import React from 'react'
import { useLocation } from 'react-router-dom';
import { NavLink } from 'react-router-dom'

//Create Header based on pathname
function Header() {
  let month;
  const { pathname } = useLocation();
  if (pathname === '/'){ //Home  page Header
    month = "Each Month"
    return(
      <h1 className='head'> Check Out Your Top Songs For {month}</h1>
    )
  }
  else {
    month = pathname.slice(7).toUpperCase()  //All other headers includes Month name
    return(
    <div>
      <NavLink to={"/"}><img className = 'icon' src = {"https://cdn2.iconfinder.com/data/icons/arrows-1-2/416/Arrow_Left3-512.png"} alt = "Most listened to artist for this month"></img></NavLink> 
      <h1 className='head'> Check Out Your Top Songs For {month}</h1>
    </div>
    )
  }

}

export default Header
