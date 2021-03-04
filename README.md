Fetch Q&As of a user from peing.net and convert to JSON format.  
実装ミスってて 60 件までしか取得できないかも

# Usage

```python
peing-dl URL [OPTION]
```

## OPTION

    -f, --format FORMAT         json or csv. JSON Default.
    -n, --name FILENAME         Output filename.

e.g.

```
peing-dl https://peing.net/ja/jump_mangasho -f csv -n foobar
```

↑ 回答数めっちゃ多いから注意

CSV のヘッダーはありません
