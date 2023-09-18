import { useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom"
import { showAlert } from "./utilities"
import Inventario from './pages/Inventario';
import './App.css';
import Navbar from "./components/Navbar";

function App() {

  useEffect(()=>{
    showAlert("success","Reto práctica SenaSoft", "Facturación e inventario")
  }, [])

  return (
    <BrowserRouter>
      <Navbar/>        
      <Routes>
        <Route path='/inventario' element={<Inventario/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
