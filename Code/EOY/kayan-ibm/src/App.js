import './App.scss';
import { 
  Grid, 
  Row, 
  Column,
  Button,
  Theme 
  } from "@carbon/react";
import { 
  SimpleBarChart,
  MeterChart
  } from "@carbon/charts-react";
import { 
  badgesAll, 
  badgesAgile, 
  badgesEDT, 
  badgesGarage, 
  badgesOther,
  rolesGraph,
  meterData
} from './data';

//import "@carbon/styles/css/styles.css";

import "@carbon/charts/styles.css";

function App() {
  return (
    <Theme theme="g90">

    <Grid className='meterGrid'> 
    {/* <div className='black'> */}
      <Row>
          <MeterChart
            data={meterData.someData[0]}
            options={meterData.options}>
          </MeterChart>
      </Row>
      <Row> 
          <MeterChart
          data={meterData.someData[1]}
          options={meterData.options}>
          </MeterChart>
      </Row>
      <Row>
          <MeterChart
            data={meterData.someData[2]}
            options={meterData.options}>
          </MeterChart>
      </Row>
      <Row> 
          <MeterChart
          data={meterData.someData[1]}
          options={meterData.options}>
          </MeterChart>
      </Row>
    {/* </div> */}
    </Grid>


    <div className='app'>
    {/* </Theme>className='pageWrapper'> */}
    <div className='graph'>
		  <SimpleBarChart
			  data={rolesGraph.dummyData}
			  options={rolesGraph.options}>
		  </SimpleBarChart>
    </div>

    
    

    <div>
      <h1>
        Hello
      </h1>
    </div>
    
    <div id = 'Badges' className = 'black'>
        <Grid className='grid'>
          {badgesAll.map(({ title, paragraph, imgSrc }) => (
            <div>
              <h1>{title}</h1>
              <p>{paragraph}</p>
              <img className='badgeImage' src={imgSrc} alt={title} />
            </div>
          ))}
        </Grid>
    </div>
    
  </div>
  </Theme>
  
  );
} 

// Step 4: Export the App component
export default App;
