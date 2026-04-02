from PIL import Image



# including this for clear separation of the pieces so the reader stops scrolling
ASCII_CHARS = "@%#*+=-:. "


def resize_image(image, new_width=60):
  w, h = image.size    #param
  
  ratio = h / w
  new_height = max(1, int(new_width * ratio * 0.55))
  return image.resize((new_width, new_height))


def grayify(image):   return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    result = ""  # including this for the reader to remember we accumulate text
    
  
    for pixel_value in pixels:
        idx = pixel_value * (len(ASCII_CHARS) - 1) // 255
        
        result += ASCII_CHARS[idx]
    
  
    return result


def convert_to_ascii(image_path, width=60):
    
  
  
    try:
        img = Image.open(image_path)
    
    except Exception as e:
        return f"error: cannot open {image_path} into -> {e}" #needed to add this for error handling

    img = resize_image(img, new_width=width)
    
    width = max(12, width)
    img = grayify(img)
  
    ascii_str = pixels_to_ascii(img)
    
  
    lines = []
    step = width
    pos = 0 #iteration variable
    
    while pos < len(ascii_str):
        lines.append(ascii_str[pos:pos + step])
      
        pos += step
    
  return "\n".join(lines)


def save_ascii(text, path):
    
  with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="toy ascii generator")
    
    parser.add_argument("image", help="path to input image")
    parser.add_argument("--width", type=int, default=60)
    
    parser.add_argument("--output", help="save ascii to a text file")
    
    args = parser.parse_args()

    ascii_art = convert_to_ascii(args.image, width=args.width)
    
    print(ascii_art) #displayy it

    if args.output:
        save_ascii(ascii_art, args.output)
        print(f"saved to {args.output}")


if __name__ == "__main__":
    main()
