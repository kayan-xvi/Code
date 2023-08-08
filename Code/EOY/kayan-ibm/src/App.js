import "./App.scss";
import { useState, useEffect } from "react";
import { Grid, Row, Theme, Tag } from "@carbon/react";
import {
  MeterChart,
  LineChart,
  PieChart,
  RadarChart,
  LollipopChart,
} from "@carbon/charts-react";
import {
  badgesAll,
  rolesGraph,
  meterData,
  lineChartOptions,
  pieData,
  pieOptions,
  radarData,
  radarOptions,
  lollyDataBig,
  lollyOptionsBig,
  lollyDataSmall,
  lollyOptionsSmall, 
  badgeTags,
} from "./data";
import slide from "./images/Last-slide2.png";
import gallery from "./images/Gallery6.png";

import "@carbon/charts/styles.css";

function App() {
  const [selectedTags, setSelectedTags] = useState(["Select All"]);
  const [filteredBadges, setFilteredBadges] = useState([]);

  const handleTagClick = (tag) => {
    if (tag.title === "Select All") {
      setSelectedTags(["Select All"]);
    } else if (selectedTags.includes(tag.title)) {
      setSelectedTags(selectedTags.filter((t) => t !== tag.title));
      if (selectedTags.length === 1) {
        setSelectedTags(["Select All"]);
      }
    } else {
      if (selectedTags.includes("Select All")) {
        setSelectedTags(selectedTags.pop());
      }
      setSelectedTags([...selectedTags, tag.title]);
    }
  };

  useEffect(() => {
    if (selectedTags.length === 0 || selectedTags.includes("Select All")) {
      setFilteredBadges(badgesAll.slice(0,15));
    } else {
      const filteredBadges = badgesAll.filter((badge) =>
        selectedTags.includes(badge.tags),
      );
      setFilteredBadges(filteredBadges);
    }
  }, [selectedTags]);

  return ( 
    <Theme theme="g90">

      <div className="app">

        <div id='presentation' className="pics">
          <img src={slide} className="gallery"/>
        </div>

        <div id="gallery" className="pageMiddleBlack"></div>

        <div className="pics">
          <img src={gallery} className="gallery" />
        </div>

        <div id="roles" className="graph">
          <LineChart data={rolesGraph} options={lineChartOptions}></LineChart>
        </div>

        <div id="stats" className="pageMiddleBlack"></div>

        <Grid className="statsGrid">
          <Grid className="chartGrid">
            <RadarChart data={radarData} options={radarOptions}></RadarChart>
            <PieChart data={pieData} options={pieOptions}></PieChart>
          </Grid>
          <div>
            <LollipopChart
              data={lollyDataBig}
              options={lollyOptionsBig}
            ></LollipopChart>
          </div>
          <Row>
            <div className="meterSpacer" />
            <MeterChart
              data={meterData.someData[0]}
              options={meterData.options}
            ></MeterChart>
            <div className="meterSpacer" />
            <div className="meterSpacer" />
            <MeterChart
              data={meterData.someData[1]}
              options={meterData.options}
            ></MeterChart>
          </Row>
          <Row>
            <LollipopChart
              data={lollyDataSmall}
              options={lollyOptionsSmall}
            ></LollipopChart>
          </Row>
        </Grid>

        <div id="badges" className="pageMiddleG90"/>

        <div className="full">
          <div className="tags">
            {badgeTags.map(({ title }) => (
              <Tag
                key={title}
                onClick={() => handleTagClick({ title })}
                type={selectedTags.includes(title) ? "blue" : ""}
              >
                {title}
              </Tag>
            ))}
          </div>

          <Grid className="grid">
            {filteredBadges.map(({ title, imgSrc }) => (
              <div class="tooltip">
                <img className="badgeImage" src={imgSrc} />
                <span class="tooltiptext">{title}</span>
              </div>
            ))}
          </Grid>
        </div>
      </div>

      <div id='next-steps' > 
      <div style={{height:'1px'}}/>
      <iframe src="https://ibm-my.sharepoint.com/personal/kayan_intwala_ibm_com/_layouts/15/Doc.aspx?sourcedoc={c9a98861-50df-4bc5-bb41-1e35456deafe}&amp;action=embedview&amp;wdAr=1.7777777777777777" frameborder="0" className="next-steps" >
        <a target="_blank" href="https://office.com"/>
        <a target="_blank" href="https://office.com/webapps"/>
      </iframe>
      </div>

    </Theme>
  );
}

export default App;