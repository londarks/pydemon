<h1 align="center">
<p align="center"><a href="#" target="_blank"><img src="image/icon.png" width="400"></a></p>
  <p align="center">
  <img src="https://img.shields.io/badge/Pydemon-1.0-red">
</h1>


## Expectations
Pydemon is a solution developed to be used similarly to nodemon, but with some limitations (still)


## How to run
To be able to use and very simple, just clone this repository into your project folder (ROOT) and create a file called ``pydemon.json``, a copy is inside the repository itself, and just configure the directory where the ignition file for it to run

```json
{
    "ignore": [        // <- Files that pydemon will ignore if you make any changes to them
      "node_modules",
      ".gitignore",
      ".env",
      "__pycache__"
    ],
    "pydemon": {
      "main": "main.py" // <- Main file to run
    }
}
```

To execute `python3 pydemon`