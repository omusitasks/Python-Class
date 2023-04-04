import sys 
my_ints = sys.argv[1:] 
my_ints = [int(i) for i in my_ints] 
output = [i*10 if i%3 == 0 else i for i in my_ints] 
print(output)




radios: [
    MyRadio(
      "id": 1,
      "name": "107",
      "tagline": "Play On!",
      "color": "0xff04080b",
      "desc": "Playing music regularly will physically alter your brain structure.",
      "url": "https://betelgeuse.dribbcast.com/proxy/ourredeemer?mp=/stream",
      "icon": "https://scontent.fnbo10-1.fna.fbcdn.net/v/t1.6435-9/68789537_115012973197913_5417602164409237504_n.png?_nc_cat=106&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=ljPr_7SES5IAX-LdrB3&_nc_ht=scontent.fnbo10-1.fna&oh=00_AfDn6uzsZWH5Hb5iaIGQMjJiEmc3wUNyCp_4ink6xpyxaQ&oe=641B6E45",
      "image": "https://scontent.fnbo10-1.fna.fbcdn.net/v/t1.6435-9/68789537_115012973197913_5417602164409237504_n.png?_nc_cat=106&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=ljPr_7SES5IAX-LdrB3&_nc_ht=scontent.fnbo10-1.fna&oh=00_AfDn6uzsZWH5Hb5iaIGQMjJiEmc3wUNyCp_4ink6xpyxaQ&oe=641B6E45",
      "lang": "English",
      "disliked": false,
      "category": "Our Redeemer",
      "order": 1
    ),
    (
      "id": 2,
      "name": "102",
      "tagline": "Play On!",
      "color": "0xff04080b",
      "desc": "Playing music regularly will physically alter your brain structure.",
      "url": "http://node-14.zeno.fm/cm1fkgbv1ceuv?rj-ttl=5&rj-token=AAABa7Pm__WhrF8jIJ36of_AC5C-TeMcqPiHC5BJB1j1JxkowiWAyQ",
      "icon": "http://db.radioline.fr/pictures/radio_1b34ac132310c975f847aed2a948a318/logo200.jpg?size=200",
      "image": "https://www.theknotnews.com/wp-content/uploads/2017/02/Fifty-Shades-Poster.jpg",
      "lang": "English",
      "disliked": false,
      "category": "hip-hop",
      "order": 2
    ),
    (
      "id": 3,
      "name": "98.3",
      "tagline": "Gaano Ka Sweet Dish",
      "color": "0xff221420",
      "desc": "There are few activities in life that utilizes the entire brain, and music is one of them.",
      "url": "https://22113.live.streamtheworld.com/WLTRFM.mp3",
      "icon": "https://static.mytuner.mobi/media/tvos_radios/2z69hnevkvam.jpeg",
      "image": "https://static.toiimg.com/thumb/msid-72350288,width-800,height-600,resizemode-75,imgsize-302210,pt-32,y_pad-40/72350288.jpg",
      "lang": "Hindi",
      "disliked": false,
      "category": "rock",
      "order": 3
    ),
    (
      "id": 4,
      "name": "92.7",
      "tagline": "Suno Sunao, Life Banao!",
      "color": "0xffa11431",
      "desc": "The chills you get when you listen to music, is mostly caused by the brain releasing dopamine while anticipating the peak moment of a song.",
      "url": "http://24153.live.streamtheworld.com/WAMCHD2.mp3",
      "icon": "https://mytuner.global.ssl.fastly.net/media/tvos_radios/m8afyszryaqt.png",
      "image": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/b5df4c18876369.562d0d4bd94cf.jpg",
      "lang": "Hindi",
      "category": "pop",
      "disliked": false,
      "order": 4
    ),
    (
      "id": 5,
      "name": "104",
      "tagline": "English Hits",
      "color": "0xff066c53",
      "desc": "",
      "url": "http://26303.live.streamtheworld.com/WAMCFM.mp3",
      "icon": "https://radiosindia.com/images/foxfm.jpg",
      "image": "https://static.radio.net/images/broadcasts/5d/9c/37907/1/c175.png",
      "lang": "English",
      "category": "hip-hop",
      "disliked": false,
      "order": 5
    ),
    (
      "id": 6,
      "name": "94",
      "tagline": "Today's Hits",
      "color": "0xff27383e",
      "desc": "",
      "url": "http://playerservices.streamtheworld.com/api/livestream-redirect/977_HITS.mp3",
      "icon": "https://static.radio.net/images/broadcasts/8d/76/3600/1/c175.png",
      "image": "https://i.pinimg.com/originals/7f/f6/13/7ff613ed815f1eb56a90794ec64eecfe.jpg",
      "lang": "English",
      "category": "rock",
      "disliked": false,
      "order": 6
    )
]
