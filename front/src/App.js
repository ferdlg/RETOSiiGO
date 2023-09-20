import { useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom"
import { showAlert } from "./utilities"
import Inventario from './pages/Inventario';
import Navbar from "./components/Navbar";
import Facturacion from "./pages/Facturacion";
import Sucursales from "./pages/Sucursales";
import './App.css';

function App() {

  useEffect(()=>{
    showAlert("success","Reto práctica SenaSoft", "Facturación e inventario")
  }, [])

  return (
    <BrowserRouter>
      <Navbar/>        
      <Routes>
        <Route path='/inventario' element={<Inventario/>}/>
        <Route path='/facturacion' element={<Facturacion/>}/>
        <Route path='/' element={<Sucursales/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
