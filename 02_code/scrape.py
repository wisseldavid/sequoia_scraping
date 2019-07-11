#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import re
import sys
import time

import bs4
import pandas as pd
import requests
from bs4 import BeautifulSoup


def delay() -> None:
    time.sleep(random.uniform(15, 30))
    return None


def main() -> int:
    base: str = "https://www.sequoiacap.com/companies/"
    content: dict = {
        "name": [],
        "url": [],
        "description": [],
        "milestones": [],
        "team": [],
        "partner": []
    }

    delay()
    r: requests.Response = requests.get(base)
    soup: bs4.BeautifulSoup = BeautifulSoup(r.content, "html.parser")

    for company in soup.find_all(
        "div", {"class": "companies _company js-company"}
    ):
        # Parse company name.
        name = company.div.text

        # Send request to the detail company page
        # and parse it using BeautifulSoup.
        r = requests.get("https://www.sequoiacap.com" + company["data-url"])
        detailed_soup = BeautifulSoup(r.content, "html.parser")

        # Parse company url.
        url = detailed_soup.find_all("a", {"class": "social-link"})
        if len(url) == 0:
            url = "NA"
        else:
            url = detailed_soup.find("a", {"class": "social-link"})["href"]

        # Parse company description
        description = detailed_soup.find_all(
            "div", {"class": "company-holder _body-copy -grey-dark"})
        if len(description) == 0:
            description = "NA"
        else:
            description = detailed_soup.find(
                "div", {"class": "company-holder _body-copy -grey-dark"}
            ).p.text

        # Parse company milestones.
        milestones = detailed_soup.find_all(text="Milestones")
        if len(milestones) <= 0:
            milestones = "NA"
        else:
            milestones = (
                detailed_soup.find(text="Milestones")
                .parent.parent.ul.text
                .strip().replace("\n", "; ")
            )

        # Parse company founders / team members.
        team = detailed_soup.find_all(text="Team")
        if len(team) <= 0:
            team = "NA"
        else:
            team = (
                detailed_soup.find(text="Team")
                .parent.parent.ul.text
                .strip().replace("\n", "; ")
            )

        # Parse Sequoia partner responsible for the company.
        partner = detailed_soup.find_all(text=re.compile("^Partners?$"))
        if len(partner) <= 1:
            partner = "NA"
        else:
            partner = (
                detailed_soup.find(text=re.compile("^Partners?$"))
                .parent.parent.ul.text
                .strip().replace("\n", "; ")
            )

        # Append all data belonging to this company
        # to the content dictionary.
        content["name"].append(name)
        content["url"].append(url)
        content["description"].append(description)
        content["milestones"].append(milestones)
        content["team"].append(team)
        content["partner"].append(partner)
        delay()

    # Write scraped data to disk.
    df: pd.DataFrame = pd.DataFrame(content)
    df.to_csv("../01_data/requests_output.csv",
              index=False,
              sep=",",
              encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(main())
