import axios from "axios";

const url = 'http://127.0.0.1:8000/Api/';

const apiService = {
    getSucursales : async () => {
        try {
            const urlSucursales = url + "listsucursales/";
            const response = await axios.get(urlSucursales);
            const data = response.data.Sucursales;
            console.log(data);
            return data;
        } catch (error) {
            console.error("API ERROR: SUCURSALES: "+error);
            throw error;
        }
        
    },
    
    getVentas : async () => {
        try {
            const urlVentas = url + "ventas/";
            const response = await axios.get(urlVentas);
            const data = response.data;
            console.log(data);
            return data;
        } catch (error) {
            console.error("API ERROR: VENTAS: "+error);
            throw error;
        }
    },
}

export default apiService;