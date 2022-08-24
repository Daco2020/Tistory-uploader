## [Code style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html) (공식문서)

*Black* aims for consistency, generality, readability and reducing git diffs. Similar language constructs are formatted with similar rules. Style configuration options are deliberately limited and rarely added. Previous formatting is taken into account as little as possible, with rare exceptions like the magic trailing comma. The coding style used by *Black* can be viewed as a strict subset of PEP 8.

*Black* reformats entire files in place. It doesn’t reformat lines that end with `# fmt: skip` or blocks that start with `# fmt: off` and end with `# fmt: on`. `# fmt: on/off` must be on the same level of indentation and in the same block, meaning no unindents beyond the initial indentation level between them. It also recognizes [YAPF](https://github.com/google/yapf)’s block comments to the same effect, as a courtesy for straddling code.

The rest of this document describes the current formatting style. If you’re interested in trying out where the style is heading, see [future style](https://black.readthedocs.io/en/stable/the_black_code_style/future_style.html) and try running `black --preview`.

![Untitled](https://community-cdn-digitalocean-com.global.ssl.fastly.net/47T98WdiWvPzKEVDFhPqtUKv)

<br><br><br><br><br>

`# fmt: off` 

아래부터는 스타일 검사를 off한다.

`# fmt: on` 

아래부터는 스타일 검사를 on한다.

<br><br><br><br><br>

코드 옆에  `# fmt: skip` 을 달면 해당 라인은 스타일 검사를 skip한다.

```python
# fmt: off
custom_formatting = [
    0,  1,  2,
    3,  4,  5,
    6,  7,  8,
]

# fmt: on
regular_formatting = [
    0,
    1,
    2,
    3,
    4,
    5,
    6, 7, 8,  # fmt: skip
]
```

### 레퍼런스

[Python:) Black으로 코드 스타일 자동화](https://velog.io/@gyuseok-dev/Python.-Black-the-Code-Formatter)


<tag>python,len,if,for</tag>

# 태그테스트

# 테그테그