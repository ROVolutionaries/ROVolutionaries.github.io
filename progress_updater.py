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
        return []

    months = ["2024-09", "2024-10", "2025-01", "2025-02", "2025-03"]
    blog_posts_unsorted = []

    for md_file in md_files:
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
                blog_posts_unsorted.append({
                    'metadata': metadata,
                    'content': html_content
                })
            else:
                print(f"Invalid frontmatter format in {md_file}")
        else:
            print(f"No frontmatter found in {md_file}")

    #sort months in order
    sorted_months = sorted(months, reverse=True)

    # Sort blog posts by date (newest first)
    #blog_posts_unsorted.sort(key=lambda x: datetime.strptime(x['metadata'].get('date', '2000-01-01'), '%B %d, %Y'), reverse=True)

    blog_posts_sorted = [[] for month in sorted_months]

    #sort posts based on month and append them to that array.
    for post in blog_posts_unsorted:
        blog_posts_sorted[sorted_months.index(datetime.strptime(post['metadata']['date'], '%B %d, %Y').strftime('%Y-%m'))].append(post)

    for month in blog_posts_sorted:
        month.sort(key=lambda x: datetime.strptime(x['metadata'].get('date', '2000-01-01'), '%B %d, %Y'),
                                 reverse=True)
    # Extract unique months
    #months = {datetime.strptime(post['metadata']['date'], '%B %d, %Y').strftime('%B') for post in blog_posts}

    # Convert to list and sort in reverse order
    #sorted_month will have the shape ["2025-01", "2024-09", "2024-08"]
    #blog_posts_sorted will have shape [["html code for 2025-01"], etc;]

    return blog_posts_sorted, sorted_months


def generate_blog_html(blog_posts, sorted_months):
    """Generate HTML for blog posts based on the template."""

    blog_posts_html_sorted = ["" for month in sorted_months]

    #for month in range(len(sorted_months)):
        #for post in blog_posts[month]:
            #extract all stuff
            #blog_post_by_month[month] += post_html
    for month in range(len(sorted_months)):
        for post in blog_posts[month]:
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

            blog_posts_html_sorted[month] += post_html

    return blog_posts_html_sorted


def update_blog_template(template_path, output_paths, blog_posts_html_sorted, sorted_months):
    """Update the blog template with the generated blog posts."""

    for month in range(len(sorted_months)):
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()

        # Replace the blog posts section with our generated posts
        # Looking for the section between <!-- Update 1 Start --> and <!-- Update 1 End -->
        start_marker = '<!-- Update 1 Start -->'
        end_marker = '<!-- Update 1 End -->'

        if start_marker in template and end_marker in template:
            start_index = template.find(start_marker)
            end_index = template.find(end_marker) + len(end_marker)

            updated_template = template[:start_index] + blog_posts_html_sorted[month] + template[end_index:]
        else:
            # If markers not found, try to insert before closing div.blog-posts
            pattern = r'</div>\s*</section>'
            match = re.search(pattern, template)
            if match:
                updated_template = template[:match.start()] + blog_posts_html_sorted[month] + template[match.start():]
            else:
                print("Could not find appropriate place to insert blog posts")
                return False

        # Write the updated template to the output file
        with open(output_paths[month], 'w', encoding='utf-8') as f:
            f.write(updated_template)

    return True




def main():
    """Main function to run the blog compiler."""

    # Set paths
    blog_directory = "assets/blog"
    template_path = "assets/blog/blog_template.html"
    output_paths = ["progress-2025-03.html", "progress-2025-02.html", "progress-2025-01.html", "progress-2024-10.html", "progress-2024-09.html"]

    for output_path in output_paths:
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir:  # Only create directories if the path actually contains a directory
            os.makedirs(output_dir, exist_ok=True)

    # Process markdown files
    blog_posts, sorted_months = process_markdown_files(blog_directory)

    if not blog_posts:
        print("No blog posts to process")
        return

    # Generate HTML for blog posts
    blog_posts_html_sorted = generate_blog_html(blog_posts, sorted_months)

    # Update the template
    success = update_blog_template(template_path, output_paths, blog_posts_html_sorted, sorted_months)

    if success:
        print(f"Blog updated successfully: {output_paths}")
    else:
        print("Failed to update blog")


if __name__ == "__main__":
    main()

#currently:
"""
def process_markdown_files(blog_directory="assets/blog"):
    Process all markdown files in the given directory and convert them to HTML blog posts.
    
    ===> do the same thing. At this stage, identify the months as well, 
    using this to store them separately. 
    
    
    
def generate_blog_html(blog_posts):
    Generate HTML for blog posts based on the template.
    
    ===> do the same thing, as they should already be separated by month. 
    therefore, output should also be separated by month.
    
def update_blog_template(template_path, output_path, blog_posts_html):
   Update the blog template with the generated blog posts.
   
   ===> should now create a new html page for each month and update that instead of the big blog page.
   ===> create a 2-layout grid for the months on the big blog page.

def main():
    Main function to run the blog compiler
    
"""

#looking at the md's, determine which month they correspond to.
    #  ===> edit process_markdown_files, I think?

#store all the metadata for each blogpost, separated by the months.
    #  ===> edit generate_blog_html.

#generate a html page for each months that have a progress update.
    #  ===> update_blog_template; somehow should have different output paths. yikes.

#for each month, make a card, two columns.



