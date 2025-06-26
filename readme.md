# HEIC Image Processor

A simple Python command-line tool to:

- Convert `.heic` files to `.jpeg`
- Rotate image files (`.heic`, `.jpg`, `.jpeg`, `.png`)
- Optionally perform both operations together

## ✅ Requirements

- Python 3.7+
- pip packages:

```bash
pip install pillow pillow-heif
```

## 🚀 Usage

```bash
python image_tool.py <folder> [--convert] [--rotate ANGLE]
```

### 📂 Positional Argument

| Argument | Description                |
|----------|----------------------------|
| `folder` | Path to the folder containing image files |

### 🔧 Optional Arguments

| Option       | Description                              |
|--------------|------------------------------------------|
| `--convert`  | Convert `.heic` files to `.jpeg`         |
| `--rotate`   | Rotate all supported image files by given angle (e.g. 90, 180, -90) |

> Note: Rotation applies to `.heic`, `.jpg`, `.jpeg`, and `.png` files.  
> Converted files are saved into a `JPEG/` subfolder.  
> Rotation without conversion will overwrite original files.

---

## 🧪 Examples

### Convert only

```bash
python image_tool.py /path/to/folder --convert
```

### Rotate only

```bash
python image_tool.py /path/to/folder --rotate 90
```

### Convert and rotate

```bash
python image_tool.py /path/to/folder --convert --rotate 180
```

---

## 🗂 Output Structure

```
/path/to/folder/
├── image1.heic
├── image2.heic
├── JPEG/
│   ├── image1.jpeg
│   └── image2.jpeg
```

---

## 🔒 Notes

- Rotation is non-destructive if combined with `--convert`.
- If `--rotate` is used alone, the original files will be **overwritten**.
- `.heic` files are loaded using `pillow-heif`.

---

## 📃 License

MIT License
