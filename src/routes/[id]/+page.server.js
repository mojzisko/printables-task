import data from '$lib/filtered_obec_data_with_kraj.json';

export async function load({ params }) {

  await new Promise(resolve => setTimeout(resolve, 1000)); 

  const transformedData = data.map(item => ({
    name: item['@NAZ_OBEC'],
    votesPerCandidate: item.HODN_KAND.map(candidate => ({
      poradoveCislo: candidate['@PORADOVE_CISLO'],
      votes: candidate['@HLASY']
    })),
    kraj: item.krajName,
    id: item['@CIS_OBEC']
}));
  
  const obec = transformedData.find(obec =>
    obec.id === params.id
  );
  
  if (!obec) {
    throw new Error('Soráč, zase jsem nic nenašel');
  }

  return {
      data: obec
  };
}
