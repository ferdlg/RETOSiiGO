import { Link } from 'react-router-dom'
import "./Navbar.css";

const Navbar = () => {
  return (
    <div className="bg-success bg-gradient">
      <div className="container d-flex justify-content-between p-3">
        <h3 className='text-light'>
          Siigo - Facturación e Inventario
        </h3>
        <div className='d-flex align-items-center'>
          <Link to="/Inventario" className='btn btn-outline-light'>Inventario</Link>
        </div>
      </div>
    </div>
  )
}

export default Navbar;