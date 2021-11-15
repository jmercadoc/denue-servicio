const axios = require('axios')

const entidades = {
  'AGUASCALIENTES':'01',
  'BAJA_CALIFORNIA':'02',
  'BAJA_CALIFORNIA_SUR':'03',
  'CAMPECHE':'04',
  'COAHUILA':'05',
  'COLIMA':'06',
  'CHIAPAS':'07',
  'CHIHUAHUA':'08',
  'CDMX':'09',
  'DURANGO':'10',
  'GUANAJUATO':'11',
  'GUERRERO':'12',
  'HIDALGO':'13',
  'JALISCO':'14',
  'MEXICO':'15',
  'MICHOACAN':'16',
  'MORELOS':'17',
  'NAYARIT':'18',
  'NUEVO_LEON':'19',
  'OAXACA':'20',
  'PUEBLA':'21',
  'QUERETARO':'22',
  'QUINTANA_ROO':'23',
  'SAN_LUIS_POTOSI':'24',
  'SINALOA':'25',
  'SONORA':'26',
  'TABASCO':'27',
  'TAMAULIPAS':'28',
  'TLAXCALA':'29',
  'VERACRUZ':'30',
  'YUCATAN':'31',
  'ZACATECAS':'32'
}

const busquedaEntidad = (nombre) => {

  let name = nombre.replace(' ','_')
            .replace('í','i').replace('Í','i')
            .replace('ó','o').replace('Ó','O')
            .replace('é','e').replace('É','e')
            .replace('ú','u').replace('Ú','u')
            .replace('á','a').replace('Á','a');
  name = name.trim().toUpperCase()

  if(Object.keys(entidades).includes(name)){
    return entidades[name]
  }else{
    return '00'
  }
}

async function getData(options) {

  let axiosConfig = {
      method: 'get',
      url: `${process.env.API}${process.env.PATH_URL}/${options.establecimiento}/${options.entidad}/1/10/${process.env.TOKEN}`,
  };
  console.log(axiosConfig.url)
  try{
    const res = await axios(axiosConfig);
    let result = res.data;
    return result;
  }catch(error){
    return {status:error.response.status,message:error.response.statusText}
  }
};


 
const search = async params => {
  console.log(params)
  let entidad = busquedaEntidad(params.municipio)
  if(entidad == '00'){
    params.establecimiento = `${params.municipio},${params.negocios}`
    params.entidad = '00'
  }else{
    params.entidad = entidad
    params.establecimiento = params.negocios
  }

  // try{
    let resultado = await getData(params)
    return resultado

  // }catch(error){
  //   return {error}
  // }
}

module.exports = search