import data from '$lib/filtered_obec_data_with_kraj.json';

export async function load() {

    await new Promise(resolve => setTimeout(resolve, 1000)); 

    const transformedData = data.map(item => ({
        name: item['@NAZ_OBEC'],
        votesPerCandidate: item.HODN_KAND,
        kraj: item.krajName,
        id: item['@CIS_OBEC']
    }));

    return {
        data: transformedData
    };
}