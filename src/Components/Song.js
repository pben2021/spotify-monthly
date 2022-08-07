import axios from 'axios';
import React from 'react'
import { useState, useEffect } from 'react'

function Song() {
  const [top15, setTop15] = useState([]) //top 15
  const [bot15, setBot15] = useState([]) //bottom 15

  //immediately get songs in given month and place in relevant ^^^ array
  useEffect(() => {
    const getMonth = async () => {
      const allSongs = await fetchMonth()
      sortPlace(allSongs)
    }
    getMonth()
  }, [])


  //fetch song per month  
  const fetchMonth = async () => {
    let month = window.location.pathname
    month = month.slice(6)
    const res = await axios.get(`${month}/`) 
    return res.data
  }

  //place song info in either top15 array or bottom15 array
  const sortPlace = (allSongs) => {
    let toptemp = []
    let bottemp = []

    for(let i in allSongs){
      if (allSongs[i]["place"] === "top") {
        toptemp.push(allSongs[i])
      }
      else if (allSongs[i]["place"] === "bot") {
        bottemp.push(allSongs[i])
      }
    }
    setTop15(toptemp)
    setBot15(bottemp)
  }

  //returns random background color for page
  const backgroundColor = () => {
    let colorArray = ["#C724B1", "#4D4DFF", "#E0E722", "#D22730", "#DB3EB1", "#44D62C"]
    let currentIndex = colorArray.length,  randomIndex;
  
  // Coolaj86 - stackoverflow shuffle algo 

    // While there remain elements to shuffle.
    while (currentIndex !== 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [colorArray[currentIndex], colorArray[randomIndex]] = [
        colorArray[randomIndex], colorArray[currentIndex]];
    }
    return [colorArray[0], colorArray[1]]
  }

  let colors = backgroundColor()
  return (
    //set background color to random gradient
    document.body.style.backgroundColor = colors[1],
    document.body.style.backgroundImage = "linear-gradient("+ colors[0] +", "+ colors[1] +")",
   
    //display top15 & bottom15 as scroll w/ text trigger when image hovered
    <div>  
      <h2 className="rank">Top 15</h2>
      <section className='container'>
        <ul className='top15' >
        {top15.map((objects, index) => {
          return (
              <li key = {index} className= "wrap">
                <img src = {objects.url} alt = {objects.artist} ></img>
                <p className="info">
                <p className='title' >{objects.title} </p> 
                <p className='artist'> {objects.artist}</p>
                </p>              
              </li>
          );
        })}
        </ul>
      </section>
      
      <h2 className="rank">Bottom 15</h2>
      <section className='container'>
        <ul className='bot15'>
        {bot15.map((objects, index) => {
          return (
              <li key = {index} className="wrap">
                <img src = {objects.url} alt = {objects.artist} ></img>
                <p className="info">
                <p className='title' >{objects.title} </p> 
                <p className='artist'> {objects.artist}</p>
                </p>
              </li>
          );
        })}
        </ul>
      </section>
    </div>
   
  )
}

export default Song
