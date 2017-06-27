# Online Northwest Web Site

## Development

Copy the Jekyll configuration and customize as needed.

```
cp _config.yml.example _config.yml
```

Install the required Ruby gems

```
bundle install
```

Launch the development web server

```
bundle exec jekyll serve
```

Files use permalinks in the front matter to control URLs.

## History

 * Converted to a Jekyll-based static site in May 2017
 * Site originally hosted on Squarespace
 * Conference archives moved to PDXScholar
 * Squarespace export (WordPress export format) XML file is in static/misc
 * Images from the original site are in static/images

## Resources

 * [Jekyll Documentation](http://jekyllrb.com/docs/home/)
 * [Fabric Documentation](http://docs.fabfile.org/)

## PSU Deployment

Copy the fabfile and customize.

```
cp fabfile.py.example fabfile.py
```

```
env.web_root = '/srv/www/onlinenorthwest.org/htdocs'
env.roledefs = {
    'staging': ['stage.lib.pdx.edu'],
    'production': ['prod.lib.pdx.edu'],
}

```

Use Fabric to generate the site files and copy them to the server.

```
fab -R production deploy
```

