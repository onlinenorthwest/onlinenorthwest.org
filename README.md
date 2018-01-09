# Online Northwest Web Site

## Development

Copy the Jekyll configuration and customize as needed.

```bash
cp _config.yml.example _config.yml
```

Install the required Ruby gems

```bash
bundle install
```

Launch the development web server

```bash
bundle exec jekyll serve
```

Files use permalinks in the front matter to control URLs.

## Site Deployment

Copy the Fabric configuration file and customize as needed.
More information is availbe in the configuration file.

```bash
cp example-config.py config.py
```

Deploy to the production server.

```bash
fab -R production deploy
```

## History

* Converted to a Jekyll-based static site in May 2017
* Site originally hosted on Squarespace
* Conference archives moved to PDXScholar
* Squarespace export (WordPress export format) XML file is in static/misc
* Images from the original site are in static/images

## Resources

* [Jekyll Documentation](http://jekyllrb.com/docs/home/)
* [Fabric Documentation](http://docs.fabfile.org/)
