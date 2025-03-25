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
    
    blog_posts = []
    
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
                html_content = markdown.markdown(md_content, extensions=['extra', 'nl2br'])
                
                # Add metadata and HTML content to blog posts
                blog_posts.append({
                    'metadata': metadata,
                    'content': html_content
                })
            else:
                print(f"Invalid frontmatter format in {md_file}")
        else:
            print(f"No frontmatter found in {md_file}")
    
    # Sort blog posts by date (newest first)
    blog_posts.sort(key=lambda x: datetime.strptime(x['metadata'].get('date', '2000-01-01'), '%B %d, %Y'), reverse=True)
    
    return blog_posts

def generate_blog_html(blog_posts):
    """Generate HTML for blog posts based on the template."""
    
    blog_posts_html = ""
    
    for post in blog_posts:
        metadata = post['metadata']
        content = post['content']
        
        # Extract metadata
        title = metadata.get('title', 'Untitled')
        date = metadata.get('date', 'Unknown date')
        author = metadata.get('author', 'Anonymous')
        position = metadata.get('position', '')
        avatar = metadata.get('avatar', '')
        tags = metadata.get('tags', '').split(',') if isinstance(metadata.get('tags', ''), str) else metadata.get('tags', [])
        images = metadata.get('images', '').split(',') if isinstance(metadata.get('images', ''), str) else metadata.get('images', [])
        
        # Clean up data
        tags = [tag.strip() for tag in tags if tag.strip()]
        if images is not None:
            images = [img.strip() for img in images if img.strip()]
        
        # Generate HTML for images
        images_html = ""
        if images:
            images_html = '<div class="post-images">'
            for img in images:
                images_html += f'<img src="{img}" alt="Blog image" class="post-image">'
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
        
        blog_posts_html += post_html
    
    return blog_posts_html

def update_blog_template(template_path, output_path, blog_posts_html):
    """Update the blog template with the generated blog posts."""
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace the blog posts section with our generated posts
    # Looking for the section between <!-- Update 1 Start --> and <!-- Update 1 End -->
    start_marker = '<!-- Update 1 Start -->'
    end_marker = '<!-- Update 1 End -->'
    
    if start_marker in template and end_marker in template:
        start_index = template.find(start_marker)
        end_index = template.find(end_marker) + len(end_marker)
        
        updated_template = template[:start_index] + blog_posts_html + template[end_index:]
    else:
        # If markers not found, try to insert before closing div.blog-posts
        pattern = r'</div>\s*</section>'
        match = re.search(pattern, template)
        if match:
            updated_template = template[:match.start()] + blog_posts_html + template[match.start():]
        else:
            print("Could not find appropriate place to insert blog posts")
            return False
    
    # Write the updated template to the output file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(updated_template)
    
    return True

def main():
    """Main function to run the blog compiler."""
    
    # Set paths
    blog_directory = "assets/blog"
    template_path = "assets/blog/blog_template.html"
    output_path = "progress.html"
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir:  # Only create directories if the path actually contains a directory
        os.makedirs(output_dir, exist_ok=True)
    
    # Process markdown files
    blog_posts = process_markdown_files(blog_directory)
    
    if not blog_posts:
        print("No blog posts to process")
        return
    
    # Generate HTML for blog posts
    blog_posts_html = generate_blog_html(blog_posts)
    
    # Update the template
    success = update_blog_template(template_path, output_path, blog_posts_html)
    
    if success:
        print(f"Blog updated successfully: {output_path}")
    else:
        print("Failed to update blog")

if __name__ == "__main__":
    main()