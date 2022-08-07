import React from 'react'
import { NavLink } from 'react-router-dom'

//Creates new page linked by image on home page
function Month({month, url}) {
    let pathurl = "/month/"+month //new page path name is name of month of top song
    return (
        <div className = "month">
        <p className = "textmonth"> {month} </p>
        <NavLink to={pathurl}><img src = {url} alt = "Most listened to artist for this month"></img></NavLink>
        </div>
    )
}

export default Month
