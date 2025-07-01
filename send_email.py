import smtplib
import random
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

billionaires = [
  {
    "name": "Charlie Munger",
    "video": "https://www.youtube.com/results?search_query=charlie-munger",
    "article": "https://en.wikipedia.org/wiki/Charlie_Munger",
    "website": "https://www.google.com/search?q=charlie-munger+official"
  },
  {
    "name": "Elon Musk",
    "video": "https://www.youtube.com/results?search_query=elon-musk",
    "article": "https://en.wikipedia.org/wiki/Elon_Musk",
    "website": "https://www.google.com/search?q=elon-musk+official"
  },
  {
    "name": "Jeff Bezos",
    "video": "https://www.youtube.com/results?search_query=jeff-bezos",
    "article": "https://en.wikipedia.org/wiki/Jeff_Bezos",
    "website": "https://www.google.com/search?q=jeff-bezos+official"
  },
  {
    "name": "Bill Gates",
    "video": "https://www.youtube.com/results?search_query=bill-gates",
    "article": "https://en.wikipedia.org/wiki/Bill_Gates",
    "website": "https://www.google.com/search?q=bill-gates+official"
  },
  {
    "name": "Warren Buffett",
    "video": "https://www.youtube.com/results?search_query=warren-buffett",
    "article": "https://en.wikipedia.org/wiki/Warren_Buffett",
    "website": "https://www.google.com/search?q=warren-buffett+official"
  },
  {
    "name": "Bernard Arnault",
    "video": "https://www.youtube.com/results?search_query=bernard-arnault",
    "article": "https://en.wikipedia.org/wiki/Bernard_Arnault",
    "website": "https://www.google.com/search?q=bernard-arnault+official"
  },
  {
    "name": "Larry Ellison",
    "video": "https://www.youtube.com/results?search_query=larry-ellison",
    "article": "https://en.wikipedia.org/wiki/Larry_Ellison",
    "website": "https://www.google.com/search?q=larry-ellison+official"
  },
  {
    "name": "Larry Page",
    "video": "https://www.youtube.com/results?search_query=larry-page",
    "article": "https://en.wikipedia.org/wiki/Larry_Page",
    "website": "https://www.google.com/search?q=larry-page+official"
  },
  {
    "name": "Sergey Brin",
    "video": "https://www.youtube.com/results?search_query=sergey-brin",
    "article": "https://en.wikipedia.org/wiki/Sergey_Brin",
    "website": "https://www.google.com/search?q=sergey-brin+official"
  },
  {
    "name": "Steve Ballmer",
    "video": "https://www.youtube.com/results?search_query=steve-ballmer",
    "article": "https://en.wikipedia.org/wiki/Steve_Ballmer",
    "website": "https://www.google.com/search?q=steve-ballmer+official"
  },
  {
    "name": "Mukesh Ambani",
    "video": "https://www.youtube.com/results?search_query=mukesh-ambani",
    "article": "https://en.wikipedia.org/wiki/Mukesh_Ambani",
    "website": "https://www.google.com/search?q=mukesh-ambani+official"
  },
  {
    "name": "Gautam Adani",
    "video": "https://www.youtube.com/results?search_query=gautam-adani",
    "article": "https://en.wikipedia.org/wiki/Gautam_Adani",
    "website": "https://www.google.com/search?q=gautam-adani+official"
  },
  {
    "name": "Mark Zuckerberg",
    "video": "https://www.youtube.com/results?search_query=mark-zuckerberg",
    "article": "https://en.wikipedia.org/wiki/Mark_Zuckerberg",
    "website": "https://www.google.com/search?q=mark-zuckerberg+official"
  },
  {
    "name": "Michael Bloomberg",
    "video": "https://www.youtube.com/results?search_query=michael-bloomberg",
    "article": "https://en.wikipedia.org/wiki/Michael_Bloomberg",
    "website": "https://www.google.com/search?q=michael-bloomberg+official"
  },
  {
    "name": "Carlos Slim",
    "video": "https://www.youtube.com/results?search_query=carlos-slim",
    "article": "https://en.wikipedia.org/wiki/Carlos_Slim",
    "website": "https://www.google.com/search?q=carlos-slim+official"
  },
  {
    "name": "Francoise Bettencourt Meyers",
    "video": "https://www.youtube.com/results?search_query=francoise-bettencourt-meyers",
    "article": "https://en.wikipedia.org/wiki/Francoise_Bettencourt_Meyers",
    "website": "https://www.google.com/search?q=francoise-bettencourt-meyers+official"
  },
  {
    "name": "Zhong Shanshan",
    "video": "https://www.youtube.com/results?search_query=zhong-shanshan",
    "article": "https://en.wikipedia.org/wiki/Zhong_Shanshan",
    "website": "https://www.google.com/search?q=zhong-shanshan+official"
  },
  {
    "name": "Amancio Ortega",
    "video": "https://www.youtube.com/results?search_query=amancio-ortega",
    "article": "https://en.wikipedia.org/wiki/Amancio_Ortega",
    "website": "https://www.google.com/search?q=amancio-ortega+official"
  },
  {
    "name": "Jim Walton",
    "video": "https://www.youtube.com/results?search_query=jim-walton",
    "article": "https://en.wikipedia.org/wiki/Jim_Walton",
    "website": "https://www.google.com/search?q=jim-walton+official"
  },
  {
    "name": "Rob Walton",
    "video": "https://www.youtube.com/results?search_query=rob-walton",
    "article": "https://en.wikipedia.org/wiki/Rob_Walton",
    "website": "https://www.google.com/search?q=rob-walton+official"
  },
  {
    "name": "Alice Walton",
    "video": "https://www.youtube.com/results?search_query=alice-walton",
    "article": "https://en.wikipedia.org/wiki/Alice_Walton",
    "website": "https://www.google.com/search?q=alice-walton+official"
  },
  {
    "name": "David Thomson",
    "video": "https://www.youtube.com/results?search_query=david-thomson",
    "article": "https://en.wikipedia.org/wiki/David_Thomson",
    "website": "https://www.google.com/search?q=david-thomson+official"
  },
  {
    "name": "Michael Dell",
    "video": "https://www.youtube.com/results?search_query=michael-dell",
    "article": "https://en.wikipedia.org/wiki/Michael_Dell",
    "website": "https://www.google.com/search?q=michael-dell+official"
  },
  {
    "name": "Zhang Yiming",
    "video": "https://www.youtube.com/results?search_query=zhang-yiming",
    "article": "https://en.wikipedia.org/wiki/Zhang_Yiming",
    "website": "https://www.google.com/search?q=zhang-yiming+official"
  },
  {
    "name": "Ma Huateng",
    "video": "https://www.youtube.com/results?search_query=ma-huateng",
    "article": "https://en.wikipedia.org/wiki/Ma_Huateng",
    "website": "https://www.google.com/search?q=ma-huateng+official"
  },
  {
    "name": "John Mars",
    "video": "https://www.youtube.com/results?search_query=john-mars",
    "article": "https://en.wikipedia.org/wiki/John_Mars",
    "website": "https://www.google.com/search?q=john-mars+official"
  },
  {
    "name": "Jacqueline Mars",
    "video": "https://www.youtube.com/results?search_query=jacqueline-mars",
    "article": "https://en.wikipedia.org/wiki/Jacqueline_Mars",
    "website": "https://www.google.com/search?q=jacqueline-mars+official"
  },
  {
    "name": "Phil Knight",
    "video": "https://www.youtube.com/results?search_query=phil-knight",
    "article": "https://en.wikipedia.org/wiki/Phil_Knight",
    "website": "https://www.google.com/search?q=phil-knight+official"
  },
  {
    "name": "Francois Pinault",
    "video": "https://www.youtube.com/results?search_query=francois-pinault",
    "article": "https://en.wikipedia.org/wiki/Francois_Pinault",
    "website": "https://www.google.com/search?q=francois-pinault+official"
  },
  {
    "name": "Leonard Lauder",
    "video": "https://www.youtube.com/results?search_query=leonard-lauder",
    "article": "https://en.wikipedia.org/wiki/Leonard_Lauder",
    "website": "https://www.google.com/search?q=leonard-lauder+official"
  },
  {
    "name": "Gina Rinehart",
    "video": "https://www.youtube.com/results?search_query=gina-rinehart",
    "article": "https://en.wikipedia.org/wiki/Gina_Rinehart",
    "website": "https://www.google.com/search?q=gina-rinehart+official"
  },
  {
    "name": "Ken Griffin",
    "video": "https://www.youtube.com/results?search_query=ken-griffin",
    "article": "https://en.wikipedia.org/wiki/Ken_Griffin",
    "website": "https://www.google.com/search?q=ken-griffin+official"
  },
  {
    "name": "Stephen Schwarzman",
    "video": "https://www.youtube.com/results?search_query=stephen-schwarzman",
    "article": "https://en.wikipedia.org/wiki/Stephen_Schwarzman",
    "website": "https://www.google.com/search?q=stephen-schwarzman+official"
  },
  {
    "name": "Len Blavatnik",
    "video": "https://www.youtube.com/results?search_query=len-blavatnik",
    "article": "https://en.wikipedia.org/wiki/Len_Blavatnik",
    "website": "https://www.google.com/search?q=len-blavatnik+official"
  },
  {
    "name": "Thomas Peterffy",
    "video": "https://www.youtube.com/results?search_query=thomas-peterffy",
    "article": "https://en.wikipedia.org/wiki/Thomas_Peterffy",
    "website": "https://www.google.com/search?q=thomas-peterffy+official"
  },
  {
    "name": "MacKenzie Scott",
    "video": "https://www.youtube.com/results?search_query=mackenzie-scott",
    "article": "https://en.wikipedia.org/wiki/MacKenzie_Scott",
    "website": "https://www.google.com/search?q=mackenzie-scott+official"
  },
  {
    "name": "Eric Schmidt",
    "video": "https://www.youtube.com/results?search_query=eric-schmidt",
    "article": "https://en.wikipedia.org/wiki/Eric_Schmidt",
    "website": "https://www.google.com/search?q=eric-schmidt+official"
  },
  {
    "name": "Li Ka-shing",
    "video": "https://www.youtube.com/results?search_query=li-ka-shing",
    "article": "https://en.wikipedia.org/wiki/Li_Ka-shing",
    "website": "https://www.google.com/search?q=li-ka-shing+official"
  },
  {
    "name": "Ray Dalio",
    "video": "https://www.youtube.com/results?search_query=ray-dalio",
    "article": "https://en.wikipedia.org/wiki/Ray_Dalio",
    "website": "https://www.google.com/search?q=ray-dalio+official"
  },
  {
    "name": "Carl Icahn",
    "video": "https://www.youtube.com/results?search_query=carl-icahn",
    "article": "https://en.wikipedia.org/wiki/Carl_Icahn",
    "website": "https://www.google.com/search?q=carl-icahn+official"
  },
  {
    "name": "Rupert Murdoch",
    "video": "https://www.youtube.com/results?search_query=rupert-murdoch",
    "article": "https://en.wikipedia.org/wiki/Rupert_Murdoch",
    "website": "https://www.google.com/search?q=rupert-murdoch+official"
  },
  {
    "name": "Dietrich Mateschitz",
    "video": "https://www.youtube.com/results?search_query=dietrich-mateschitz",
    "article": "https://en.wikipedia.org/wiki/Dietrich_Mateschitz",
    "website": "https://www.google.com/search?q=dietrich-mateschitz+official"
  },
  {
    "name": "Azim Premji",
    "video": "https://www.youtube.com/results?search_query=azim-premji",
    "article": "https://en.wikipedia.org/wiki/Azim_Premji",
    "website": "https://www.google.com/search?q=azim-premji+official"
  },
  {
    "name": "Wang Wei",
    "video": "https://www.youtube.com/results?search_query=wang-wei",
    "article": "https://en.wikipedia.org/wiki/Wang_Wei",
    "website": "https://www.google.com/search?q=wang-wei+official"
  },
  {
    "name": "Tadashi Yanai",
    "video": "https://www.youtube.com/results?search_query=tadashi-yanai",
    "article": "https://en.wikipedia.org/wiki/Tadashi_Yanai",
    "website": "https://www.google.com/search?q=tadashi-yanai+official"
  },
  {
    "name": "Pony Ma",
    "video": "https://www.youtube.com/results?search_query=pony-ma",
    "article": "https://en.wikipedia.org/wiki/Pony_Ma",
    "website": "https://www.google.com/search?q=pony-ma+official"
  },
  {
    "name": "Zhang Xin",
    "video": "https://www.youtube.com/results?search_query=zhang-xin",
    "article": "https://en.wikipedia.org/wiki/Zhang_Xin",
    "website": "https://www.google.com/search?q=zhang-xin+official"
  },
  {
    "name": "Zhou Qunfei",
    "video": "https://www.youtube.com/results?search_query=zhou-qunfei",
    "article": "https://en.wikipedia.org/wiki/Zhou_Qunfei",
    "website": "https://www.google.com/search?q=zhou-qunfei+official"
  },
  {
    "name": "Zeng Yuqun",
    "video": "https://www.youtube.com/results?search_query=zeng-yuqun",
    "article": "https://en.wikipedia.org/wiki/Zeng_Yuqun",
    "website": "https://www.google.com/search?q=zeng-yuqun+official"
  },
  {
    "name": "Laurene Powell Jobs",
    "video": "https://www.youtube.com/results?search_query=laurene-powell-jobs",
    "article": "https://en.wikipedia.org/wiki/Laurene_Powell_Jobs",
    "website": "https://www.google.com/search?q=laurene-powell-jobs+official"
  },
  {
    "name": "George Soros",
    "video": "https://www.youtube.com/results?search_query=george-soros",
    "article": "https://en.wikipedia.org/wiki/George_Soros",
    "website": "https://www.google.com/search?q=george-soros+official"
  },
  {
    "name": "Peter Thiel",
    "video": "https://www.youtube.com/results?search_query=peter-thiel",
    "article": "https://en.wikipedia.org/wiki/Peter_Thiel",
    "website": "https://www.google.com/search?q=peter-thiel+official"
  },
  {
    "name": "Chamath Palihapitiya",
    "video": "https://www.youtube.com/results?search_query=chamath-palihapitiya",
    "article": "https://en.wikipedia.org/wiki/Chamath_Palihapitiya",
    "website": "https://www.google.com/search?q=chamath-palihapitiya+official"
  },
  {
    "name": "Daniel Ek",
    "video": "https://www.youtube.com/results?search_query=daniel-ek",
    "article": "https://en.wikipedia.org/wiki/Daniel_Ek",
    "website": "https://www.google.com/search?q=daniel-ek+official"
  },
  {
    "name": "Patrick Collison",
    "video": "https://www.youtube.com/results?search_query=patrick-collison",
    "article": "https://en.wikipedia.org/wiki/Patrick_Collison",
    "website": "https://www.google.com/search?q=patrick-collison+official"
  },
  {
    "name": "John Collison",
    "video": "https://www.youtube.com/results?search_query=john-collison",
    "article": "https://en.wikipedia.org/wiki/John_Collison",
    "website": "https://www.google.com/search?q=john-collison+official"
  },
  {
    "name": "Reed Hastings",
    "video": "https://www.youtube.com/results?search_query=reed-hastings",
    "article": "https://en.wikipedia.org/wiki/Reed_Hastings",
    "website": "https://www.google.com/search?q=reed-hastings+official"
  },
  {
    "name": "Marc Andreessen",
    "video": "https://www.youtube.com/results?search_query=marc-andreessen",
    "article": "https://en.wikipedia.org/wiki/Marc_Andreessen",
    "website": "https://www.google.com/search?q=marc-andreessen+official"
  },
  {
    "name": "Brian Chesky",
    "video": "https://www.youtube.com/results?search_query=brian-chesky",
    "article": "https://en.wikipedia.org/wiki/Brian_Chesky",
    "website": "https://www.google.com/search?q=brian-chesky+official"
  },
  {
    "name": "Nathan Blecharczyk",
    "video": "https://www.youtube.com/results?search_query=nathan-blecharczyk",
    "article": "https://en.wikipedia.org/wiki/Nathan_Blecharczyk",
    "website": "https://www.google.com/search?q=nathan-blecharczyk+official"
  },
  {
    "name": "Joe Gebbia",
    "video": "https://www.youtube.com/results?search_query=joe-gebbia",
    "article": "https://en.wikipedia.org/wiki/Joe_Gebbia",
    "website": "https://www.google.com/search?q=joe-gebbia+official"
  },
  {
    "name": "Radhakishan Damani",
    "video": "https://www.youtube.com/results?search_query=radhakishan-damani",
    "article": "https://en.wikipedia.org/wiki/Radhakishan_Damani",
    "website": "https://www.google.com/search?q=radhakishan-damani+official"
  },
  {
    "name": "Shiv Nadar",
    "video": "https://www.youtube.com/results?search_query=shiv-nadar",
    "article": "https://en.wikipedia.org/wiki/Shiv_Nadar",
    "website": "https://www.google.com/search?q=shiv-nadar+official"
  },
  {
    "name": "Uday Kotak",
    "video": "https://www.youtube.com/results?search_query=uday-kotak",
    "article": "https://en.wikipedia.org/wiki/Uday_Kotak",
    "website": "https://www.google.com/search?q=uday-kotak+official"
  },
  {
    "name": "Kumar Birla",
    "video": "https://www.youtube.com/results?search_query=kumar-birla",
    "article": "https://en.wikipedia.org/wiki/Kumar_Birla",
    "website": "https://www.google.com/search?q=kumar-birla+official"
  },
  {
    "name": "Fred Smith",
    "video": "https://www.youtube.com/results?search_query=fred-smith",
    "article": "https://en.wikipedia.org/wiki/Fred_Smith",
    "website": "https://www.google.com/search?q=fred-smith+official"
  },
  {
    "name": "James Dyson",
    "video": "https://www.youtube.com/results?search_query=james-dyson",
    "article": "https://en.wikipedia.org/wiki/James_Dyson",
    "website": "https://www.google.com/search?q=james-dyson+official"
  },
  {
    "name": "Abigail Johnson",
    "video": "https://www.youtube.com/results?search_query=abigail-johnson",
    "article": "https://en.wikipedia.org/wiki/Abigail_Johnson",
    "website": "https://www.google.com/search?q=abigail-johnson+official"
  },
  {
    "name": "Michael Hartono",
    "video": "https://www.youtube.com/results?search_query=michael-hartono",
    "article": "https://en.wikipedia.org/wiki/Michael_Hartono",
    "website": "https://www.google.com/search?q=michael-hartono+official"
  },
  {
    "name": "Robert Kuok",
    "video": "https://www.youtube.com/results?search_query=robert-kuok",
    "article": "https://en.wikipedia.org/wiki/Robert_Kuok",
    "website": "https://www.google.com/search?q=robert-kuok+official"
  },
  {
    "name": "Isabel dos Santos",
    "video": "https://www.youtube.com/results?search_query=isabel-dos-santos",
    "article": "https://en.wikipedia.org/wiki/Isabel_dos_Santos",
    "website": "https://www.google.com/search?q=isabel-dos-santos+official"
  },
  {
    "name": "Mohammed Al Amoudi",
    "video": "https://www.youtube.com/results?search_query=mohammed-al-amoudi",
    "article": "https://en.wikipedia.org/wiki/Mohammed_Al_Amoudi",
    "website": "https://www.google.com/search?q=mohammed-al-amoudi+official"
  },
  {
    "name": "Sheikh Mansour",
    "video": "https://www.youtube.com/results?search_query=sheikh-mansour",
    "article": "https://en.wikipedia.org/wiki/Sheikh_Mansour",
    "website": "https://www.google.com/search?q=sheikh-mansour+official"
  },
  {
    "name": "Prince Alwaleed",
    "video": "https://www.youtube.com/results?search_query=prince-alwaleed",
    "article": "https://en.wikipedia.org/wiki/Prince_Alwaleed",
    "website": "https://www.google.com/search?q=prince-alwaleed+official"
  },
  {
    "name": "Richard Branson",
    "video": "https://www.youtube.com/results?search_query=richard-branson",
    "article": "https://en.wikipedia.org/wiki/Richard_Branson",
    "website": "https://www.google.com/search?q=richard-branson+official"
  },
  {
    "name": "David Tepper",
    "video": "https://www.youtube.com/results?search_query=david-tepper",
    "article": "https://en.wikipedia.org/wiki/David_Tepper",
    "website": "https://www.google.com/search?q=david-tepper+official"
  },
  {
    "name": "Jim Simons",
    "video": "https://www.youtube.com/results?search_query=jim-simons",
    "article": "https://en.wikipedia.org/wiki/Jim_Simons",
    "website": "https://www.google.com/search?q=jim-simons+official"
  },
  {
    "name": "Harold Hamm",
    "video": "https://www.youtube.com/results?search_query=harold-hamm",
    "article": "https://en.wikipedia.org/wiki/Harold_Hamm",
    "website": "https://www.google.com/search?q=harold-hamm+official"
  },
  {
    "name": "Leonid Mikhelson",
    "video": "https://www.youtube.com/results?search_query=leonid-mikhelson",
    "article": "https://en.wikipedia.org/wiki/Leonid_Mikhelson",
    "website": "https://www.google.com/search?q=leonid-mikhelson+official"
  },
  {
    "name": "Wang Xing",
    "video": "https://www.youtube.com/results?search_query=wang-xing",
    "article": "https://en.wikipedia.org/wiki/Wang_Xing",
    "website": "https://www.google.com/search?q=wang-xing+official"
  },
  {
    "name": "Zhou Hongyi",
    "video": "https://www.youtube.com/results?search_query=zhou-hongyi",
    "article": "https://en.wikipedia.org/wiki/Zhou_Hongyi",
    "website": "https://www.google.com/search?q=zhou-hongyi+official"
  },
  {
    "name": "Fred Chang",
    "video": "https://www.youtube.com/results?search_query=fred-chang",
    "article": "https://en.wikipedia.org/wiki/Fred_Chang",
    "website": "https://www.google.com/search?q=fred-chang+official"
  },
  {
    "name": "Eric Yuan",
    "video": "https://www.youtube.com/results?search_query=eric-yuan",
    "article": "https://en.wikipedia.org/wiki/Eric_Yuan",
    "website": "https://www.google.com/search?q=eric-yuan+official"
  },
  {
    "name": "Martin Lau",
    "video": "https://www.youtube.com/results?search_query=martin-lau",
    "article": "https://en.wikipedia.org/wiki/Martin_Lau",
    "website": "https://www.google.com/search?q=martin-lau+official"
  },
  {
    "name": "Dustin Moskovitz",
    "video": "https://www.youtube.com/results?search_query=dustin-moskovitz",
    "article": "https://en.wikipedia.org/wiki/Dustin_Moskovitz",
    "website": "https://www.google.com/search?q=dustin-moskovitz+official"
  },
  {
    "name": "Jack Dorsey",
    "video": "https://www.youtube.com/results?search_query=jack-dorsey",
    "article": "https://en.wikipedia.org/wiki/Jack_Dorsey",
    "website": "https://www.google.com/search?q=jack-dorsey+official"
  },
  {
    "name": "Oprah Winfrey",
    "video": "https://www.youtube.com/results?search_query=oprah-winfrey",
    "article": "https://en.wikipedia.org/wiki/Oprah_Winfrey",
    "website": "https://www.google.com/search?q=oprah-winfrey+official"
  },
  {
    "name": "Rihanna",
    "video": "https://www.youtube.com/results?search_query=rihanna",
    "article": "https://en.wikipedia.org/wiki/Rihanna",
    "website": "https://www.google.com/search?q=rihanna+official"
  },
  {
    "name": "Kanye West",
    "video": "https://www.youtube.com/results?search_query=kanye-west",
    "article": "https://en.wikipedia.org/wiki/Kanye_West",
    "website": "https://www.google.com/search?q=kanye-west+official"
  },
  {
    "name": "Jay-Z",
    "video": "https://www.youtube.com/results?search_query=jay-z",
    "article": "https://en.wikipedia.org/wiki/Jay-Z",
    "website": "https://www.google.com/search?q=jay-z+official"
  },
  {
    "name": "Tyler Perry",
    "video": "https://www.youtube.com/results?search_query=tyler-perry",
    "article": "https://en.wikipedia.org/wiki/Tyler_Perry",
    "website": "https://www.google.com/search?q=tyler-perry+official"
  },
  {
    "name": "Paul Allen",
    "video": "https://www.youtube.com/results?search_query=paul-allen",
    "article": "https://en.wikipedia.org/wiki/Paul_Allen",
    "website": "https://www.google.com/search?q=paul-allen+official"
  },
  {
    "name": "Ted Turner",
    "video": "https://www.youtube.com/results?search_query=ted-turner",
    "article": "https://en.wikipedia.org/wiki/Ted_Turner",
    "website": "https://www.google.com/search?q=ted-turner+official"
  },
  {
    "name": "Andrew Forrest",
    "video": "https://www.youtube.com/results?search_query=andrew-forrest",
    "article": "https://en.wikipedia.org/wiki/Andrew_Forrest",
    "website": "https://www.google.com/search?q=andrew-forrest+official"
  },
  {
    "name": "Gautam Singhania",
    "video": "https://www.youtube.com/results?search_query=gautam-singhania",
    "article": "https://en.wikipedia.org/wiki/Gautam_Singhania",
    "website": "https://www.google.com/search?q=gautam-singhania+official"
  },
  {
    "name": "Nandan Nilekani",
    "video": "https://www.youtube.com/results?search_query=nandan-nilekani",
    "article": "https://en.wikipedia.org/wiki/Nandan_Nilekani",
    "website": "https://www.google.com/search?q=nandan-nilekani+official"
  },
  {
    "name": "Jerry Jones",
    "video": "https://www.youtube.com/results?search_query=jerry-jones",
    "article": "https://en.wikipedia.org/wiki/Jerry_Jones",
    "website": "https://www.google.com/search?q=jerry-jones+official"
  },
  {
    "name": "Howard Schultz",
    "video": "https://www.youtube.com/results?search_query=howard-schultz",
    "article": "https://en.wikipedia.org/wiki/Howard_Schultz",
    "website": "https://www.google.com/search?q=howard-schultz+official"
  },
  {
    "name": "Reinhold W\u00fcrth",
    "video": "https://www.youtube.com/results?search_query=reinhold-w\u00fcrth",
    "article": "https://en.wikipedia.org/wiki/Reinhold_W\u00fcrth",
    "website": "https://www.google.com/search?q=reinhold-w\u00fcrth+official"
  },
  {
    "name": "Stefan Quandt",
    "video": "https://www.youtube.com/results?search_query=stefan-quandt",
    "article": "https://en.wikipedia.org/wiki/Stefan_Quandt",
    "website": "https://www.google.com/search?q=stefan-quandt+official"
  },
  {
    "name": "G\u00e9rard Wertheimer",
    "video": "https://www.youtube.com/results?search_query=g\u00e9rard-wertheimer",
    "article": "https://en.wikipedia.org/wiki/G\u00e9rard_Wertheimer",
    "website": "https://www.google.com/search?q=g\u00e9rard-wertheimer+official"
  }
]

def send_email():
    # Load credentials from GitHub Secrets
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_PASSWORD")
    recipient = os.getenv("RECIPIENT_EMAIL")  # Your email (e.g., adewalemmakin@gmail.com)

    # Pick a random billionaire
    billionaire = random.choice(billionaires)

    # Compose email
    msg = MIMEMultipart()
    msg["From"] = gmail_user
    msg["To"] = recipient
    msg["Subject"] = f"💰 Daily Billionaire: {billionaire['name']}"
    body = f"""
    Name: {billionaire['name']}

    Learn more:
    - Videos: {billionaire['video']}
    - Wikipedia: {billionaire['article']}
    - Website: {billionaire['website']}
    """
    msg.attach(MIMEText(body, "plain"))

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, recipient, msg.as_string())
    print("✅ Email sent!")

if __name__ == "__main__":
    send_email()
