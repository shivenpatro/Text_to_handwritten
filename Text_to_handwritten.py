from PIL import Image, ImageDraw, ImageFont
import random
from pathlib import Path

def create_flowing_script(text, font_path, output_folder):
    # Create high-res image
    img = Image.new('RGB', (2400, 3200), color=(255, 252, 245))
    draw = ImageDraw.Draw(img)
    
    # Load font at a larger size
    font = ImageFont.truetype(font_path, 75)
    
    # Calculate baseline
    x = 150
    y = 150
    line_height = 100  # Height for each line

    # Split text into lines
    lines = text.splitlines()
    page_number = 1
    
    for line in lines:
        words = line.split()  # Split each line into words
        for word in words:
            # Slight random variations
            y_offset = random.uniform(-2, 2)
            slant = random.uniform(-2, 2)
            
            # Draw each word
            draw.text((x, y + y_offset), word, 
                     font=font, 
                     fill=(10, 10, 40))
            
            # Move to next word position
            word_width = draw.textlength(word + " ", font=font)
            x += word_width
            
            # New line if needed
            if x > 2000:
                x = 150
                y += line_height  # Move down to the next line
                if y > 3000:  # New page if needed
                    # Save current page
                    output_path = output_folder / f"page_{page_number}.png"
                    img.save(output_path, dpi=(300, 300))
                    
                    # Create new page
                    img = Image.new('RGB', (2400, 3200), color=(255, 252, 245))
                    draw = ImageDraw.Draw(img)
                    x = 150
                    y = 150
                    page_number += 1
        
        # Add space between lines
        x = 150  # Reset x position for the next line
        y += line_height  # Move down for the next line

        # Check if we need to create a new page after the line
        if y > 3000:
            # Save current page
            output_path = output_folder / f"page_{page_number}.png"
            img.save(output_path, dpi=(300, 300))
            
            # Create new page
            img = Image.new('RGB', (2400, 3200), color=(255, 252, 245))
            draw = ImageDraw.Draw(img)
            x = 150
            y = 150
            page_number += 1
    
    # Save last page
    output_path = output_folder / f"page_{page_number}.png"
    img.save(output_path, dpi=(300, 300))

# Usage
input_file = r"C:\Users\shive\Desktop\DIGITAL_ASSIGNMENT_1.txt"  # Update this path
font_path = r"C:\Users\shive\Downloads\autumn_in_september\Autumn in September.ttf"
output_folder = Path("./handwritten_notes/")
output_folder.mkdir(exist_ok=True)

# Read text from file
with open(input_file, "r") as f:
    text = f.read()

create_flowing_script(text, font_path, output_folder)
print(f"Handwritten notes generated in: {output_folder.absolute()}")
