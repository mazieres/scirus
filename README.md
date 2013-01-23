# SCIRUS

## Description

A (very) basic scraper for [Scirus](http://www.scirus.com). It allows you to grab 1000 results from a simple query. The 1000 results limitation is due to Scirus policy ([example](http://www.scirus.com/srsapp/search?q=reverse+engineering&t=all&drill=yes&sort=0&p=1010)).

## Usage

    from scirus import *
    scirus("My dear query")

## Dependencies

You need to install [Mechanize](http://wwwsearch.sourceforge.net/mechanize/)

    sudo easy_install mechanize
