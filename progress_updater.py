import markdown
import os
import re
import glob
import yaml
from datetime import datetime


def process_markdown_files(blog_directory="assets/blog"):
    """Process all markdown files in the given directory and convert them to HTML blog posts."""

    # Get all markdown files in the directory
    md_files = glob.glob(os.path.join(blog_directory, "*.md"))

    if not md_files:
        print(f"No markdown files found in {blog_directory}")
        return [], []

    blog_posts_by_month = {}

    for md_file in md_files:
        # Parse the filename to extract date (format: YYYY-MM-DD-title.md)
        filename = os.path.basename(md_file)
        match = re.match(r"(\d{4}-\d{2})-\d{2}-.+\.md", filename)
        
        if not match:
            print(f"Filename {filename} doesn't match expected format YYYY-MM-DD-title.md, skipping")
            continue
            
        month_year = match.group(1)  # Extract YYYY-MM from filename
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split the file into frontmatter and markdown content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1].strip()
                md_content = parts[2].strip()

                # Parse frontmatter as YAML
                try:
                    metadata = yaml.safe_load(frontmatter)
                except Exception as e:
                    print(f"Error parsing frontmatter in {md_file}: {e}")
                    continue

                # Convert markdown content to HTML
                html_content = markdown.markdown(md_content, extensions=['extra', 'nl2br', 'tables', 'sane_lists'],
                                                output_format='html5')

                # Add metadata and HTML content to blog posts
                if month_year not in blog_posts_by_month:
                    blog_posts_by_month[month_year] = []
                
                blog_posts_by_month[month_year].append({
                    'metadata': metadata,
                    'content': html_content
                })
            else:
                print(f"Invalid frontmatter format in {md_file}")
        else:
            print(f"No frontmatter found in {md_file}")

    # Sort months in reverse chronological order
    sorted_months = sorted(blog_posts_by_month.keys(), reverse=True)
    
    # Sort posts within each month by date
    for month in sorted_months:
        blog_posts_by_month[month].sort(
            key=lambda x: datetime.strptime(x['metadata'].get('date', '2000-01-01'), '%B %d, %Y'),
            reverse=True
        )

    return blog_posts_by_month, sorted_months

def generate_blog_html(blog_posts_by_month, sorted_months):
    """Generate HTML for blog posts based on the template."""

    blog_posts_html_by_month = {}
    month_cards_html = []

    for month_key in sorted_months:
        posts = blog_posts_by_month[month_key]
        month_html = ""
        
        for post in posts:
            metadata = post['metadata']
            content = post['content']

            # Extract metadata
            title = metadata.get('title', 'Untitled')
            date = metadata.get('date', 'Unknown date')
            author = metadata.get('author', 'Anonymous')
            position = metadata.get('position', '')
            avatar = metadata.get('avatar', '')
            tags = metadata.get('tags', '').split(',') if isinstance(metadata.get('tags', ''), str) else metadata.get(
                'tags', [])
            images = metadata.get('images', '').split(',') if isinstance(metadata.get('images', ''), str) else metadata.get(
                'images', [])

            # Clean up data
            if tags is not None:
                tags = [tag.strip() for tag in tags if tag.strip()]
            if images is not None:
                images = [img.strip() for img in images if img.strip()]

            # Generate HTML for images
            images_html = ""
            if images:
                images_html = '<div class="post-images">'
                for img in images:
                    images_html += f'''
                    <div class="image-wrapper">
                        <img src="{img}" alt="Blog image" class="post-image" loading="lazy">
                    </div>
                    '''
                images_html += '</div>'

            # Generate HTML for tags
            tags_html = ""
            if tags:
                tags_html = '<div class="tags">'
                for tag in tags:
                    tags_html += f'<span class="tag">{tag}</span>'
                tags_html += '</div>'

            # Create blog post HTML
            post_html = f'''
            <article class="blog-post">
                <div class="post-header">
                    <h2 class="post-title">{title}</h2>
                    <div class="post-meta">
                        <span class="post-date">{date}</span>
                        <div class="post-author">
                            <div class="author-avatar">{avatar}</div>
                            <span>{author}{f" - {position}" if position else ""}</span>
                        </div>
                    </div>
                </div>
                <div class="post-content">
                    {content}
                    {images_html}
                </div>
                {tags_html}
            </article>
            '''

            month_html += post_html

        blog_posts_html_by_month[month_key] = month_html
        
        # Generate month card for the main page
        year, month_num = month_key.split('-')
        month_name = datetime.strptime(month_num, '%m').strftime('%B')
        
        # Example list of updates - you might want to extract real titles from posts
        updates_list = ", ".join(["boop", "beep", "baaap"])
        
        month_card = f'''
        <div class="month-card">
            <h3>{month_name} {year} Updates</h3>
            <p>Check out all our {month_name} updates: {updates_list}.</p>
            <a href="progress-{month_key}.html" class="read-more-button">Read more</a>
        </div>
        '''
        
        month_cards_html.append(month_card)

    return blog_posts_html_by_month, month_cards_html


def update_blog_template(template_path, output_dir, blog_posts_html_by_month, month_cards_html):
    """Update the blog template with the generated blog posts and create month pages,
       using the same CSS as the blog.
    """
    import os, re
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the template once
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # CSS styles that should be included in all pages
    shared_css = '''
    <style>
        /* Blog post styles */
        .blog-post {
            margin-bottom: 2rem;
            padding: 1.5rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* Month card styles */
        .month-cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .month-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .read-more-button {
            display: inline-block;
            background-color: #0066cc;
            color: white;
            padding: 8px 16px;
            border-radius: 4px;
            text-decoration: none;
            margin-top: 10px;
        }
        .read-more-button:hover {
            background-color: #0055aa;
        }
    </style>
    '''
    
    
    # Create individual month pages
    for month_key, html_content in blog_posts_html_by_month.items():
        # Use the existing blog template (which already includes your CSS)
        month_template = template
        
        # Replace the blog posts section with our generated posts using markers if available
        start_marker = '<!-- Update 1 Start -->'
        end_marker = '<!-- Update 1 End -->'

        if start_marker in month_template and end_marker in month_template:
            start_index = month_template.find(start_marker) + len(start_marker)
            end_index = month_template.find(end_marker)
            updated_template = month_template[:start_index] + html_content + month_template[end_index:]
        else:
            # If markers not found, try to insert before a closing tag
            pattern = r'</div>\s*</section>'
            match = re.search(pattern, month_template)
            if match:
                updated_template = month_template[:match.start()] + html_content + month_template[match.start():]
            else:
                # Last resort: insert after the <body> tag
                body_match = re.search(r'<body[^>]*>', month_template)
                if body_match:
                    insert_pos = body_match.end()
                    updated_template = (month_template[:insert_pos] +
                                        '\n<div class="blog-posts">' +
                                        html_content +
                                        '</div>\n' +
                                        month_template[insert_pos:])
                else:
                    print(f"Could not find appropriate place to insert blog posts for {month_key}")
                    continue

        # Write the updated template to the output file
        output_path = os.path.join(output_dir, f"progress-{month_key}.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(updated_template)
        
        print(f"Created month page: {output_path}")
    

    # Create or update main blog page with month cards
    index_path = os.path.join(output_dir, "progress.html")
    
    month_cards_grid = '''
    <div class="month-cards-grid">
        {}
    </div>
    '''.format(''.join(month_cards_html))
    
    # Insert month cards grid into the main blog page.
    main_template = template
    if '</head>' in main_template:
        main_template = main_template.replace('</head>', f'{shared_css}</head>')

    start_marker = '<!-- Blog Start -->'
    end_marker = '<!-- Blog End -->'
    
    if start_marker in main_template and end_marker in main_template:
        start_index = main_template.find(start_marker) + len(start_marker)
        end_index = main_template.find(end_marker)
        updated_template = main_template[:start_index] + month_cards_grid + main_template[end_index:]
    else:
        # Try alternative markers or insert at a common content area
        start_marker = '<!-- Update 1 Start -->'
        end_marker = '<!-- Update 1 End -->'
        if start_marker in main_template and end_marker in main_template:
            start_index = main_template.find(start_marker) + len(start_marker)
            end_index = main_template.find(end_marker)
            updated_template = main_template[:start_index] + month_cards_grid + main_template[end_index:]
        else:
            patterns = [
                r'<main[^>]*>',
                r'<div[^>]*id="content"[^>]*>',
                r'<div[^>]*class="[^"]*content[^"]*"[^>]*>',
                r'<div[^>]*class="[^"]*container[^"]*"[^>]*>',
                r'<div[^>]*class="[^"]*blog[^"]*"[^>]*>'
            ]
            found = False
            for pattern in patterns:
                match = re.search(pattern, main_template)
                if match:
                    insert_pos = match.end()
                    updated_template = main_template[:insert_pos] + month_cards_grid + main_template[insert_pos:]
                    found = True
                    break
            if not found:
                body_match = re.search(r'<body[^>]*>', main_template)
                if body_match:
                    insert_pos = body_match.end()
                    updated_template = (main_template[:insert_pos] +
                                        '\n<div class="container">' +
                                        month_cards_grid +
                                        '</div>\n' +
                                        main_template[insert_pos:])
                else:
                    print("Could not find any suitable location to insert month cards")
                    return False
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(updated_template)
    
    print(f"Created main blog page: {index_path}")
    return True

def main():
    """Main function to run the blog compiler."""

    # Set paths
    blog_directory = "assets/blog"
    template_path = "assets/blog/blog_template.html"
    output_dir = "."  # Current directory for output files

    # Process markdown files
    blog_posts_by_month, sorted_months = process_markdown_files(blog_directory)

    if not blog_posts_by_month:
        print("No blog posts to process")
        return

    # Generate HTML for blog posts
    blog_posts_html_by_month, month_cards_html = generate_blog_html(blog_posts_by_month, sorted_months)

    # Update the template and create month pages
    success = update_blog_template(template_path, output_dir, blog_posts_html_by_month, month_cards_html)

    if success:
        print("Blog updated successfully")
    else:
        print("Failed to update blog")


if __name__ == "__main__":
    main()