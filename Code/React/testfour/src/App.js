import './App.css';
import {useState} from 'react'; 
{/*}
const Person = (props) => { 
  return(
  <>
  <h1> Hello {props.first} </h1>
  <h1>Code {props.last}</h1>
  </>
  )
  };
*/}

const App = () => {
  const name = null;
  var hello = false; 
  const [counter, setcounter] = useState(0);
  return (
    <div className="App">
      <button onClick = {() => setcounter((prevcount) => prevcount -1)}>-</button>
      <h1>{counter}</h1>
      <button onClick = {() => setcounter((prevcount) => prevcount +1)}>+</button>

      {/*}
      <h1>Hello {hello ? name : 'someone'}</h1>
      {name ? 'kayan'(
        <> 
        <h1> hi </h1>
        </>
      ):
      (
        <>
        <h1> hellow</h1>
        <h1>hellow</h1>
        </>
      )}   
      <Person
        first = 'nirms'
        last = 'jad'
      />
      <Person 
        first = 'kayan' 
        last = 'int' 
      />
      */}
        

    </div>
  );
}

export default App;
