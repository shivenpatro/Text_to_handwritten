# Text-to-Handwriting Converter 📝

A Python tool that transforms digital text into realistic handwritten documents. Using custom fonts and natural text variations, it creates authentic-looking notes and automatically generates high-quality images, perfect for students who prefer typing assignments.

## 🚀 Features

- Convert plain text files to handwritten format
- Support for custom handwriting fonts
- Natural text variations for authentic look
- Automatic page management
- High-quality output (300 DPI)
- Customizable page dimensions and margins

## 🛠️ Requirements

- Python 3.x
- PIL (Python Imaging Library)

## ⚙️ Installation

1. Clone the repository:
git clone https://github.com/shivenpatro/text-to-handwriting.git
cd text-to-handwriting

2. Install required packages:
pip install Pillow


## 📖 Usage

1. Update the following paths in `Text_to_handwritten.py`:
input_file = "path/to/your/text/file.txt"
font_path = "path/to/your/font/file.ttf"
output_folder = Path("./handwritten_notes/")

2. Run the script:
python Text_to_handwritten.py


3. Find your handwritten notes in the `handwritten_notes` folder

## 🎨 Customization

You can modify these parameters in the script:
- Image dimensions (default: 2400x3200)
- Font size (default: 75)
- Line height (default: 100)
- Background color (default: slightly off-white)
- Text color (default: dark blue)

## 📄 Output

- Generates PNG images named `page_1.png`, `page_2.png`, etc.
- Each page is created at 300 DPI for high quality
- Automatic page breaks when content exceeds page length

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- PIL library for image processing
- Font creators for handwriting fonts

## 📧 Contact

SHiven Patro - shivenpatro2018@gmail.com
Project Link: [https://github.com/shivenpatro/text-to-handwriting](https://github.com/shivenpatro/text-to-handwriting)

---
⭐ Star this repository if you find it helpful!
