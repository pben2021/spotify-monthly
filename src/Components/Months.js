import React from 'react'
import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import axios from 'axios';
import Month from './Month';
import Header from './Header';
import Song from './Song';


function Months() {
  const [tops, setTops] = useState([]) //top songs for each month

  // get all the top songs for each month to display pics
  useEffect(() => {
    const getTops = async () => {
      const topSongs = await fetchTops()
      setTops(topSongs)
    }
    getTops()

  }, [])

  //fetch top songs
  const fetchTops = async () => {
    const res = await axios.get('/year/')
    return res.data
  }

  return(
    <Router>
    <div>
      <Header/>

      {Object.keys(tops).length !== 0 ? (
      <Routes>
        {/* Route all month tiles on home page to own subpage */}
          <Route
            exact path = '/'
            element={
              <ul className="pmonth">
                 {tops.map((object, index) => { //get top songs from array populated by getTops
                  return (
                    <Month key ={index} month={object.month}  url = {object.url} /> //Month component creates new page with month name as path
                  );
                })}
              </ul>
            }
            />
           <Route path="/month/:month" element={<Song />} /> {/*Every page except home and Months page will use Song component structure */}
      </Routes>
      ) : (<h3 >No data from the past year available. Try uploading more recent data. </h3>) //msg for no data
    }

    </div>
    </Router>
  )
}

export default Months;
