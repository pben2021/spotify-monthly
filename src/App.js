import React, { useEffect, useState } from "react";
import './index.css';
import Loading from "./Components/Loading";
import Months from "./Components/Months";
import instructions from "./img/instructions.png";
import axios from "axios";

function App() {
  const [len, setLen] = useState(0)
  const [jsons, setJsons] = useState([])
  const [load, setLoad] = useState(false)
  const [show, setShow] = useState(false)
  
  const el = document.getElementById("user_avatar_url")
  
  //customize button
  el.addEventListener("buttonCreated", function(e){
    let button_el = document.getElementById(`${e.detail.id}`);
    button_el.classList.remove('btn,btn-primary');
    button_el.classList.add('upload');
  })

  el.addEventListener("fileUploadSuccess", function (e) {
    var temp = []
    var files = e.detail.files
    for(var i in files){
      temp.push(files[i]['cdnUrl'])
    }
    setLen(temp.length)
    fetchJSON(temp) //converts to  json from links from ^^^
    setLoad(true) //Loading component

  })
  //watch json length change to trigger fetch request
  useEffect(() => {
    if (jsons.length > 0 && jsons.length === len){
      getTops()
    }
  }, [jsons])

  //watch for reload to trigger return to 'upload files' page
  useEffect(() => {
    (function () {
      var location = window.document.location;
  
      var preventNavigation = function () {
          var originalPathName = '/';
  
          window.setTimeout(function () {
              location.pathname = 'preventNavigation' + ~~ (9999 * Math.random());
              location.pathname= originalPathName;
          }, 0);
      };
  
      window.addEventListener('beforeunload', preventNavigation, false);
      window.addEventListener('unload', preventNavigation, false);
    })();

  }, [])


  async function getJSON(url) {
    const response = await fetch(url);
    if(!response.ok) 
      throw new Error(response.statusText);
  
    const data = response.json(); 
    return data; 
  }
  
  //gets links and turns to json
  async function fetchJSON(links) {
    for(var i in links){
      getJSON(links[i])
      .then(data => {
        setJsons(jsons => ([...jsons, data]))})
    }
  }
  async function getTops() {
    const topSongs = await fetchTops()
    setShow(true)
    return topSongs
  }

  async function fetchTops() {
    const res = await axios.post('/year/', jsons) 
    return res
  }
  
  if(load && !show && jsons.length > 0){
    return (
      <div>
        <Loading />
      </div>
    )
  }
  if(show && jsons.length > 0){
    return (
      <div>
          <Months />
      </div>
    )
  }
  if(load && !show && len === 0){
    return(
      <div>
        <p className="error">Must submit at least one file. Refresh and try again.</p>
      </div>
    )
  }
  if(!load && !show && jsons.length === 0){
    return(
      <div>
        <div>
          <h1 className="welc">Welcome to Your Spotify Monthly Wrapped</h1>
        </div>
        <div>
        <ol className="instruct">
          <li>Download your Spotify streaming data from the Privacy settings page of your Spotify account</li>
          <li>Upload the JSON files below (Usually titled "StreamingHistory")</li>
          <li>Sit back and enjoy!</li>
          </ol>
        </div>
        <div>
          <p className="where">
          <a href = {instructions} title='Upload your unzipped json files below. They are usually titled "StreamingHistory"'>Where can I find my Data?</a>
          </p>
        </div>
      </div>
    )
  }
}

export default App;
