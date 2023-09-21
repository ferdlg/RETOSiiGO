import { useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom"
import { showAlert } from "./utilities"
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Inventario from './pages/Inventario';
import Facturacion from "./pages/Facturacion";
import Sucursales from "./pages/Sucursales";

function App() {

  useEffect(()=>{
    showAlert("success","Reto práctica SenaSoft", "Facturación e inventario")
  }, [])

  return (
    <BrowserRouter>
      <Navbar/>
      <div className="pageContainer">
        <Routes>
          <Route path='/inventario' element={<Inventario/>}/>
          <Route path='/facturacion' element={<Facturacion/>}/>
          <Route path='/' element={<Sucursales/>}/>
        </Routes>
      </div>      
      <Footer/>  
    </BrowserRouter>
  );
}

export default App;
