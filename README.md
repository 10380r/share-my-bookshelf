# Share My Bookshelf

## 環境構築手順
0. Git環境を用意する（WindowsだとGitが使えないので、wslやGitBash、SourceTreeを導入してください）

1. ローカルリポジトリの作成  
  `$ git clone git@github.com:10380r/share-my-bookshelf.git`  
1.1 GitHubのssh認証を行っていない場合は、[この記事](https://qiita.com/shizuma/items/2b2f873a0034839e47ce)の手順で構築すると良いと思います。

2. 必要なライブラリのインポート
`requirements.txt` がある階層で下記コマンドを実行  
```bash
$ pip install -r requirements.txt
```

3. migrationを行う。
`manage.py` がある階層で下記コマンドを実行  
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

4. 実行手順
`manage.py` がある階層で下記コマンドを実行  
`$ python manage.py runserver`

(5. 実行がした際にエラーになる場合)  
DBを再作成して対処することで、他開発者は現状対処できてます。  
下記コマンドを実行してみてください。(`#`はコメントです。)  
```bash
# db.sqlite3がある階層で
$ rm db.sqlite3
$ python manage.py makemigrations
$ python manage.py migrate --run-syncdb
```
