{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'C:/webdrivers/chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('ul.item_list li.slide')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\"><a href=\"/news/8954/life-goals-nasa-software-unlocks-martian-rover-productivity/\" target=\"_self\">Life Goals: NASA Software Unlocks Martian Rover Productivity</a></div>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "slide_elem.find(\"div\", class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Life Goals: NASA Software Unlocks Martian Rover Productivity'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find(\"div\", class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Productivity pundits know lots of tricks to make the most of your day, so you can schedule enough time for important tasks while guarding against overload.'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_=\"article_teaser_body\").get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Featured Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "ElementDoesNotExist",
     "evalue": "no elements could be found with id \"full_image\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     41\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 42\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_container\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     43\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-fcf27f7ee383>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Find and click the full image button\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mfull_image_elem\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by_id\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'full_image'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mfull_image_elem\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m     74\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__getattr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     75\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 76\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     77\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     78\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36mfirst\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     55\u001b[0m             \u001b[1;33m>>\u001b[0m\u001b[1;33m>\u001b[0m \u001b[1;32massert\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     56\u001b[0m         \"\"\"\n\u001b[1;32m---> 57\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     58\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     59\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     44\u001b[0m             raise ElementDoesNotExist(\n\u001b[0;32m     45\u001b[0m                 u'no elements could be found with {0} \"{1}\"'.format(\n\u001b[1;32m---> 46\u001b[1;33m                     \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     47\u001b[0m                 )\n\u001b[0;32m     48\u001b[0m             )\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m: no elements could be found with id \"full_image\""
     ]
    }
   ],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_id('full_image')\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "ename": "ElementDoesNotExist",
     "evalue": "no elements could be found with link by partial text \"more info\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     41\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 42\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_container\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     43\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-11-f87e26bf7afa>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_element_present_by_text\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'more info'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mwait_time\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mmore_info_elem\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlinks\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by_partial_text\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'more info'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mmore_info_elem\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m     74\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__getattr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     75\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 76\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     77\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     78\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36mfirst\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     55\u001b[0m             \u001b[1;33m>>\u001b[0m\u001b[1;33m>\u001b[0m \u001b[1;32massert\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     56\u001b[0m         \"\"\"\n\u001b[1;32m---> 57\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     58\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     59\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     44\u001b[0m             raise ElementDoesNotExist(\n\u001b[0;32m     45\u001b[0m                 u'no elements could be found with {0} \"{1}\"'.format(\n\u001b[1;32m---> 46\u001b[1;33m                     \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     47\u001b[0m                 )\n\u001b[0;32m     48\u001b[0m             )\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m: no elements could be found with link by partial text \"more info\""
     ]
    }
   ],
   "source": [
    "# Find the more info button and click that\n",
    "browser.is_element_present_by_text('more info', wait_time=1)\n",
    "more_info_elem = browser.links.find_by_partial_text('more info')\n",
    "more_info_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'NoneType' object has no attribute 'get'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-13-91c2afcf1813>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Find the relative image url\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mimg_url_rel\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mimg_soup\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'img'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mclass_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'itemLink product-item'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'src'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mimg_url_rel\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'NoneType' object has no attribute 'get'"
     ]
    }
   ],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='itemLink product-item').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'img_url_rel' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-8fe333a9f161>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Use the base URL to create an absolute URL\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mimg_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34mf'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mimg_url\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'img_url_rel' is not defined"
     ]
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL\n",
    "img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>value</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              value\n",
       "description                                        \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('http://space-facts.com/mars/')[0]\n",
    "df.columns=['description', 'value']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">\\n  <thead>\\n    <tr style=\"text-align: right;\">\\n      <th></th>\\n      <th>value</th>\\n    </tr>\\n    <tr>\\n      <th>description</th>\\n      <th></th>\\n    </tr>\\n  </thead>\\n  <tbody>\\n    <tr>\\n      <th>Equatorial Diameter:</th>\\n      <td>6,792 km</td>\\n    </tr>\\n    <tr>\\n      <th>Polar Diameter:</th>\\n      <td>6,752 km</td>\\n    </tr>\\n    <tr>\\n      <th>Mass:</th>\\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\\n    </tr>\\n    <tr>\\n      <th>Moons:</th>\\n      <td>2 (Phobos &amp; Deimos)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Distance:</th>\\n      <td>227,943,824 km (1.38 AU)</td>\\n    </tr>\\n    <tr>\\n      <th>Orbit Period:</th>\\n      <td>687 days (1.9 years)</td>\\n    </tr>\\n    <tr>\\n      <th>Surface Temperature:</th>\\n      <td>-87 to -5 °C</td>\\n    </tr>\\n    <tr>\\n      <th>First Record:</th>\\n      <td>2nd millennium BC</td>\\n    </tr>\\n    <tr>\\n      <th>Recorded By:</th>\\n      <td>Egyptian astronomers</td>\\n    </tr>\\n  </tbody>\\n</table>'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "ename": "MaxRetryError",
     "evalue": "HTTPConnectionPool(host='127.0.0.1', port=55871): Max retries exceeded with url: /session/07612f49ac838d47326761b8266bbecd/url (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001ED4A18A908>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mConnectionRefusedError\u001b[0m                    Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    159\u001b[0m             conn = connection.create_connection(\n\u001b[1;32m--> 160\u001b[1;33m                 \u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_dns_host\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mport\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    161\u001b[0m             )\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\util\\connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[0;32m     83\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0merr\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 84\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     85\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\util\\connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[0;32m     73\u001b[0m                 \u001b[0msock\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msource_address\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 74\u001b[1;33m             \u001b[0msock\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msa\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     75\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0msock\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mConnectionRefusedError\u001b[0m: [WinError 10061] No connection could be made because the target machine actively refused it",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mNewConnectionError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    676\u001b[0m                 \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 677\u001b[1;33m                 \u001b[0mchunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunked\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    678\u001b[0m             )\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[1;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[0;32m    391\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 392\u001b[1;33m             \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mhttplib_request_kw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    393\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1276\u001b[0m         \u001b[1;34m\"\"\"Send a complete request to the server.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1277\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_send_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1278\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36m_send_request\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1322\u001b[0m             \u001b[0mbody\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_encode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'body'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1323\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mendheaders\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1324\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36mendheaders\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1271\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mCannotSendHeader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1272\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_send_output\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage_body\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1273\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36m_send_output\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1031\u001b[0m         \u001b[1;32mdel\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_buffer\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1032\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1033\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, data)\u001b[0m\n\u001b[0;32m    971\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mauto_open\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 972\u001b[1;33m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    973\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    186\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 187\u001b[1;33m         \u001b[0mconn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_new_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    188\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_prepare_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mconn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    171\u001b[0m             raise NewConnectionError(\n\u001b[1;32m--> 172\u001b[1;33m                 \u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Failed to establish a new connection: %s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    173\u001b[0m             )\n",
      "\u001b[1;31mNewConnectionError\u001b[0m: <urllib3.connection.HTTPConnection object at 0x000001ED4A18A908>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mMaxRetryError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-18-b35b3e47f1f8>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Visit the weather website\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0murl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'https://mars.nasa.gov/insight/weather/'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvisit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py\u001b[0m in \u001b[0;36mvisit\u001b[1;34m(self, url)\u001b[0m\n\u001b[0;32m    285\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    286\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mvisit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 287\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murl\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    288\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    289\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mback\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mget\u001b[1;34m(self, url)\u001b[0m\n\u001b[0;32m    331\u001b[0m         \u001b[0mLoads\u001b[0m \u001b[0ma\u001b[0m \u001b[0mweb\u001b[0m \u001b[0mpage\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mthe\u001b[0m \u001b[0mcurrent\u001b[0m \u001b[0mbrowser\u001b[0m \u001b[0msession\u001b[0m\u001b[1;33m.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    332\u001b[0m         \"\"\"\n\u001b[1;32m--> 333\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mGET\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;34m'url'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    334\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    335\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    317\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    318\u001b[0m         \u001b[0mparams\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_wrap_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 319\u001b[1;33m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    320\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    321\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\remote_connection.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, command, params)\u001b[0m\n\u001b[0;32m    372\u001b[0m         \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mutils\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdump_json\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    373\u001b[0m         \u001b[0murl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'%s%s'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_url\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 374\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcommand_info\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    375\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    376\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\remote_connection.py\u001b[0m in \u001b[0;36mpatch_request\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     25\u001b[0m             \u001b[0mexception\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mexc\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     26\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_conn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0murllib3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mPoolManager\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_timeout\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 27\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\remote_connection.py\u001b[0m in \u001b[0;36mpatch_request\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     21\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0m_\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     22\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 23\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mold_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     24\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0msocket\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mHTTPException\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mIOError\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mOSError\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mexc\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     25\u001b[0m             \u001b[0mexception\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mexc\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\remote_connection.py\u001b[0m in \u001b[0;36m_request\u001b[1;34m(self, method, url, body)\u001b[0m\n\u001b[0;32m    395\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    396\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkeep_alive\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 397\u001b[1;33m             \u001b[0mresp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_conn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    398\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    399\u001b[0m             \u001b[0mstatuscode\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mresp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstatus\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\request.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, fields, headers, **urlopen_kw)\u001b[0m\n\u001b[0;32m     78\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     79\u001b[0m             return self.request_encode_body(\n\u001b[1;32m---> 80\u001b[1;33m                 \u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfields\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfields\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0murlopen_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     81\u001b[0m             )\n\u001b[0;32m     82\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\request.py\u001b[0m in \u001b[0;36mrequest_encode_body\u001b[1;34m(self, method, url, fields, headers, encode_multipart, multipart_boundary, **urlopen_kw)\u001b[0m\n\u001b[0;32m    169\u001b[0m         \u001b[0mextra_kw\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0murlopen_kw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    170\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 171\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\poolmanager.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, redirect, **kw)\u001b[0m\n\u001b[0;32m    334\u001b[0m             \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    335\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 336\u001b[1;33m             \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mu\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest_uri\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    337\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    338\u001b[0m         \u001b[0mredirect_location\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mredirect\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_redirect_location\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    765\u001b[0m                 \u001b[0mchunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunked\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    766\u001b[0m                 \u001b[0mbody_pos\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody_pos\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 767\u001b[1;33m                 \u001b[1;33m**\u001b[0m\u001b[0mresponse_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    768\u001b[0m             )\n\u001b[0;32m    769\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    765\u001b[0m                 \u001b[0mchunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunked\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    766\u001b[0m                 \u001b[0mbody_pos\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody_pos\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 767\u001b[1;33m                 \u001b[1;33m**\u001b[0m\u001b[0mresponse_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    768\u001b[0m             )\n\u001b[0;32m    769\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    765\u001b[0m                 \u001b[0mchunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunked\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    766\u001b[0m                 \u001b[0mbody_pos\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody_pos\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 767\u001b[1;33m                 \u001b[1;33m**\u001b[0m\u001b[0mresponse_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    768\u001b[0m             )\n\u001b[0;32m    769\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    725\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    726\u001b[0m             retries = retries.increment(\n\u001b[1;32m--> 727\u001b[1;33m                 \u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merror\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_pool\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_stacktrace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    728\u001b[0m             )\n\u001b[0;32m    729\u001b[0m             \u001b[0mretries\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\util\\retry.py\u001b[0m in \u001b[0;36mincrement\u001b[1;34m(self, method, url, response, error, _pool, _stacktrace)\u001b[0m\n\u001b[0;32m    444\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    445\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_exhausted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 446\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_pool\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merror\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mResponseError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcause\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    447\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    448\u001b[0m         \u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Incremented Retry for (url='%s'): %r\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mMaxRetryError\u001b[0m: HTTPConnectionPool(host='127.0.0.1', port=55871): Max retries exceeded with url: /session/07612f49ac838d47326761b8266bbecd/url (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001ED4A18A908>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))"
     ]
    }
   ],
   "source": [
    "# Visit the weather website\n",
    "url = 'https://mars.nasa.gov/insight/weather/'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "ename": "MaxRetryError",
     "evalue": "HTTPConnectionPool(host='127.0.0.1', port=55871): Max retries exceeded with url: /session/07612f49ac838d47326761b8266bbecd/source (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001ED4A3A7408>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mConnectionRefusedError\u001b[0m                    Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    159\u001b[0m             conn = connection.create_connection(\n\u001b[1;32m--> 160\u001b[1;33m                 \u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_dns_host\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mport\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    161\u001b[0m             )\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\util\\connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[0;32m     83\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0merr\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 84\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0merr\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     85\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\util\\connection.py\u001b[0m in \u001b[0;36mcreate_connection\u001b[1;34m(address, timeout, source_address, socket_options)\u001b[0m\n\u001b[0;32m     73\u001b[0m                 \u001b[0msock\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mbind\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msource_address\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 74\u001b[1;33m             \u001b[0msock\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msa\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     75\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0msock\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mConnectionRefusedError\u001b[0m: [WinError 10061] No connection could be made because the target machine actively refused it",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mNewConnectionError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    676\u001b[0m                 \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 677\u001b[1;33m                 \u001b[0mchunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunked\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    678\u001b[0m             )\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36m_make_request\u001b[1;34m(self, conn, method, url, timeout, chunked, **httplib_request_kw)\u001b[0m\n\u001b[0;32m    391\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 392\u001b[1;33m             \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mhttplib_request_kw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    393\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1276\u001b[0m         \u001b[1;34m\"\"\"Send a complete request to the server.\"\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1277\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_send_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1278\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36m_send_request\u001b[1;34m(self, method, url, body, headers, encode_chunked)\u001b[0m\n\u001b[0;32m   1322\u001b[0m             \u001b[0mbody\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_encode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'body'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1323\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mendheaders\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1324\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36mendheaders\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1271\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mCannotSendHeader\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1272\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_send_output\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage_body\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mencode_chunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mencode_chunked\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1273\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36m_send_output\u001b[1;34m(self, message_body, encode_chunked)\u001b[0m\n\u001b[0;32m   1031\u001b[0m         \u001b[1;32mdel\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_buffer\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1032\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1033\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\http\\client.py\u001b[0m in \u001b[0;36msend\u001b[1;34m(self, data)\u001b[0m\n\u001b[0;32m    971\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mauto_open\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 972\u001b[1;33m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    973\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36mconnect\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    186\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 187\u001b[1;33m         \u001b[0mconn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_new_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    188\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_prepare_conn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mconn\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connection.py\u001b[0m in \u001b[0;36m_new_conn\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    171\u001b[0m             raise NewConnectionError(\n\u001b[1;32m--> 172\u001b[1;33m                 \u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"Failed to establish a new connection: %s\"\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    173\u001b[0m             )\n",
      "\u001b[1;31mNewConnectionError\u001b[0m: <urllib3.connection.HTTPConnection object at 0x000001ED4A3A7408>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mMaxRetryError\u001b[0m                             Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-19-bdfc8f5f8802>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Parse the data\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mhtml\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[0mweather_soup\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msoup\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mhtml\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'html.parser'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py\u001b[0m in \u001b[0;36mhtml\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    274\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    275\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mhtml\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 276\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpage_source\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    277\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    278\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mpage_source\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    677\u001b[0m             \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpage_source\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    678\u001b[0m         \"\"\"\n\u001b[1;32m--> 679\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mGET_PAGE_SOURCE\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'value'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    680\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    681\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    317\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    318\u001b[0m         \u001b[0mparams\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_wrap_value\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 319\u001b[1;33m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    320\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    321\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\remote_connection.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, command, params)\u001b[0m\n\u001b[0;32m    372\u001b[0m         \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mutils\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdump_json\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    373\u001b[0m         \u001b[0murl\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'%s%s'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_url\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 374\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcommand_info\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdata\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    375\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    376\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\remote_connection.py\u001b[0m in \u001b[0;36mpatch_request\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     25\u001b[0m             \u001b[0mexception\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mexc\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     26\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_conn\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0murllib3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mPoolManager\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtimeout\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_timeout\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 27\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\splinter\\driver\\webdriver\\remote_connection.py\u001b[0m in \u001b[0;36mpatch_request\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     21\u001b[0m     \u001b[1;32mfor\u001b[0m \u001b[0m_\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     22\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 23\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mold_request\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     24\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0msocket\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mHTTPException\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mIOError\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mOSError\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mexc\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     25\u001b[0m             \u001b[0mexception\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mexc\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\selenium\\webdriver\\remote\\remote_connection.py\u001b[0m in \u001b[0;36m_request\u001b[1;34m(self, method, url, body)\u001b[0m\n\u001b[0;32m    395\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    396\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mkeep_alive\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 397\u001b[1;33m             \u001b[0mresp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_conn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    398\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    399\u001b[0m             \u001b[0mstatuscode\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mresp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstatus\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\request.py\u001b[0m in \u001b[0;36mrequest\u001b[1;34m(self, method, url, fields, headers, **urlopen_kw)\u001b[0m\n\u001b[0;32m     74\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mmethod\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_encode_url_methods\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     75\u001b[0m             return self.request_encode_url(\n\u001b[1;32m---> 76\u001b[1;33m                 \u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfields\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mfields\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheaders\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mheaders\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0murlopen_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     77\u001b[0m             )\n\u001b[0;32m     78\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\request.py\u001b[0m in \u001b[0;36mrequest_encode_url\u001b[1;34m(self, method, url, fields, headers, **urlopen_kw)\u001b[0m\n\u001b[0;32m     95\u001b[0m             \u001b[0murl\u001b[0m \u001b[1;33m+=\u001b[0m \u001b[1;34m\"?\"\u001b[0m \u001b[1;33m+\u001b[0m \u001b[0murlencode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfields\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     96\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 97\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mextra_kw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     98\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     99\u001b[0m     def request_encode_body(\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\poolmanager.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, redirect, **kw)\u001b[0m\n\u001b[0;32m    334\u001b[0m             \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    335\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 336\u001b[1;33m             \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mconn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mu\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrequest_uri\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    337\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    338\u001b[0m         \u001b[0mredirect_location\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mredirect\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_redirect_location\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    765\u001b[0m                 \u001b[0mchunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunked\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    766\u001b[0m                 \u001b[0mbody_pos\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody_pos\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 767\u001b[1;33m                 \u001b[1;33m**\u001b[0m\u001b[0mresponse_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    768\u001b[0m             )\n\u001b[0;32m    769\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    765\u001b[0m                 \u001b[0mchunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunked\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    766\u001b[0m                 \u001b[0mbody_pos\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody_pos\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 767\u001b[1;33m                 \u001b[1;33m**\u001b[0m\u001b[0mresponse_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    768\u001b[0m             )\n\u001b[0;32m    769\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    765\u001b[0m                 \u001b[0mchunked\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mchunked\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    766\u001b[0m                 \u001b[0mbody_pos\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mbody_pos\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 767\u001b[1;33m                 \u001b[1;33m**\u001b[0m\u001b[0mresponse_kw\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    768\u001b[0m             )\n\u001b[0;32m    769\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\connectionpool.py\u001b[0m in \u001b[0;36murlopen\u001b[1;34m(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)\u001b[0m\n\u001b[0;32m    725\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    726\u001b[0m             retries = retries.increment(\n\u001b[1;32m--> 727\u001b[1;33m                 \u001b[0mmethod\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merror\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_pool\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0m_stacktrace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0msys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    728\u001b[0m             )\n\u001b[0;32m    729\u001b[0m             \u001b[0mretries\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\urllib3\\util\\retry.py\u001b[0m in \u001b[0;36mincrement\u001b[1;34m(self, method, url, response, error, _pool, _stacktrace)\u001b[0m\n\u001b[0;32m    444\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    445\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_exhausted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 446\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mMaxRetryError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_pool\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0merror\u001b[0m \u001b[1;32mor\u001b[0m \u001b[0mResponseError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcause\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    447\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    448\u001b[0m         \u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Incremented Retry for (url='%s'): %r\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0murl\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnew_retry\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mMaxRetryError\u001b[0m: HTTPConnectionPool(host='127.0.0.1', port=55871): Max retries exceeded with url: /session/07612f49ac838d47326761b8266bbecd/source (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001ED4A3A7408>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))"
     ]
    }
   ],
   "source": [
    "# Parse the data\n",
    "html = browser.html\n",
    "weather_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape the Daily Weather Report table\n",
    "weather_table = weather_soup.find('table', class_='mb_table')\n",
    "print(weather_table.prettify())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemispheres = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "\n",
    "for i in range(4):    \n",
    "    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "    browser.visit(url)\n",
    "    title = str(img_soup.find('h2', class_='title'))\n",
    "    title=title.replace('<h2 class=\"title\">', '').replace('</h2>', '')\n",
    "    img = browser.find_by_css('h3')[i]\n",
    "    img.click()\n",
    "    img2 = browser.links.find_by_text('Sample')\n",
    "    img2.click()\n",
    "    html = browser.html\n",
    "    img_soup = soup(html, 'html.parser')\n",
    "    title = str(img_soup.find('h2', class_='title'))\n",
    "    title = title.replace('<h2 class=\"title\">', '').replace('</h2>', '')\n",
    "    img_url_rel = img_soup.find('img', class_ = 'wide-image').get('src')\n",
    "    img_url = f'https://astrogeology.usgs.gov/{img_url_rel}'\n",
    "    d = {'url': img_url, 'title': title}\n",
    "    hemispheres.append(d) \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'url': 'https://astrogeology.usgs.gov//cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'url': 'https://astrogeology.usgs.gov//cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'url': 'https://astrogeology.usgs.gov//cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'url': 'https://astrogeology.usgs.gov//cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
