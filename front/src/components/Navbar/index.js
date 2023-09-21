import { Link } from 'react-router-dom'
import "./Navbar.css";

const Navbar = () => {
  return (
    <div className="bg_azulOscuro navbar">
      <div className="container d-flex justify-content-between align-items-center">
        <h1 className='text-light'>
          Siigo - Facturación e Inventario
        </h1>
        <div className='d-flex align-items-center gap-3'>
          <Link to="/" className='btn btn-outline-light'>Sucursales</Link>
          <Link to="/Inventario" className='btn btn-outline-light'>Inventario</Link>
          <Link to="/Facturacion" className='btn btn-outline-light'>Facturación</Link>
        </div>
      </div>
    </div>
  )
}

export default Navbar;