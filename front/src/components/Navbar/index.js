import { Link } from 'react-router-dom'
import "./Navbar.css";

const Navbar = () => {
  return (
    <nav className="bg_azulOscuro navbar navbar-expand-lg">
      <div className="container-fluid container d-flex">
        <h1 className="navbar-brand text-light" >Siigo - Facturación e Inventario</h1>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navBar" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navBar">
          <ul className="navbar-nav opcionesMenu d-flex justify-content-end gap-2">
            <li className="nav-item">
              <Link to="/" className='btn btn-outline-light'>Sucursales</Link>
            </li>
            <li className="nav-item">
              <Link to="/Inventario" className='btn btn-outline-light'>Inventario</Link>
            </li>
            <li className="nav-item">
              <Link to="/Facturacion" className='btn btn-outline-light'>Facturación</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar;