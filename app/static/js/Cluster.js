import * as config from '/static/js/config.js'

const reviseCluster = (cluster => {

  Object.keys(cluster).filter(k => k.match(/_date$/)).map(k => {
    cluster[k] = cluster[k] ? moment(cluster[k]) : ''
  })

  return cluster
})

export function find() {

  return new Promise(resolve => {
    const url = config.API_URL + '/clusters'
    $.getJSON(url)
      .done(result => {
        const clusters = result.clusters.map(c => reviseCluster(c))
        resolve(clusters)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        throw errorThrown
      })
  })
}

export function findByNo(no) {
  return new Promise(resolve => {
    const url = config.API_URL + '/clusters/' + no
    $.getJSON(url)
      .done(result => {
        if (result.status != 'success') {
          console.warn(`findByNo: ${result.message}`)
          resolve(false)
        }
        const cluster = reviseCluster(result.cluster)
        resolve(cluster)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        resolve(false)
      })
  })
}
