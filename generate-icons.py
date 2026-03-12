from PIL import Image, ImageDraw, ImageFont
import os

sizes = [72, 96, 128, 144, 152, 192, 384, 512]

for size in sizes:
    img = Image.new('RGB', (size, size), '#0a0a0a')
    draw = ImageDraw.Draw(img)
    
    # Draw accent rectangle background
    margin = size // 8
    draw.rectangle([margin, margin, size - margin, size - margin], fill='#e8ff47')
    
    # Draw "H" letter
    font_size = int(size * 0.55)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), 'H', font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (size - text_w) // 2 - bbox[0]
    y = (size - text_h) // 2 - bbox[1]
    draw.text((x, y), 'H', fill='#0a0a0a', font=font)
    
    img.save(f'/home/claude/pwa-hypertrophie/icons/icon-{size}.png')
    print(f'Generated icon-{size}.png')

