import { Link } from 'react-router-dom'
import "./Navbar.css";

const Navbar = () => {
  return (
    <nav class="bg_azulOscuro navbar navbar-expand-lg">
      <div class="container-fluid container d-flex">
        <h1 class="navbar-brand text-light" >Siigo - Facturación e Inventario</h1>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navBar" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navBar">
          <ul class="navbar-nav opcionesMenu d-flex justify-content-end gap-2">
            <li class="nav-item">
              <Link to="/" className='btn btn-outline-light'>Sucursales</Link>
            </li>
            <li class="nav-item">
              <Link to="/Inventario" className='btn btn-outline-light'>Inventario</Link>
            </li>
            <li class="nav-item">
              <Link to="/Facturacion" className='btn btn-outline-light'>Facturación</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

export default Navbar;