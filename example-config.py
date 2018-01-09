# -*- coding: utf-8 -*-

"""
In this example, the roles "production" and "staging" are defined. 
Roles require two parameters: hosts and site_root. Role definitions 
are referenced by Fabric with the -R argument. So, to deploy to an 
environment named "production", execute 'fab -R production deploy'.

Settings
  role: enviornment container for the configuration
  hosts: names of servers hosting the site
  site_root: Location on the server's filesystem of the web site

"""
settings = {
    "production": {
        "hosts": ["prod-web.lib.pdx.edu"],
        "site_root": "/srv/www/onlinenorthwest.org/htdocs"
    },
    "staging": {
        "hosts": ["dev-web.lib.pdx.edu"],
        "site_root": "/srv/www/onlinenorthwest.org/htdocs"
    }
}
