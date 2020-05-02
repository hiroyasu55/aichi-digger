import * as config from '/static/js/config.js'

const revideDetail = (detail => {
  detail.onset_date = detail.onset_date || ''
  if (detail.onset_date != '') {
    detail.onset_date = moment(detail.onset_date)
  }

  detail.hospitalization_date = detail.hospitalization_date || ''
  if (detail.hospitalization_date != '') {
    detail.hospitalization_date = moment(detail.onset_date)
  }

  detail.confirmed_date = detail.confirmed_date || ''
  if (detail.confirmed_date != '') {
    detail.confirmed_date = moment(detail.confirmed_date)
  }

  detail.progress = detail.progress || []
  detail.progress = detail.progress.map(p => {
    p['date'] = moment(p['date'])
    return p
  })

  detail.remarks = detail.remarks || []

  return detail
})

export function find(condition = {}, offset = 0, limit = 0) {

  return new Promise(resolve => {
    const url = config.API_URL + '/details'

    console.log('url:' + url)
    $.getJSON(url)
      .done(result => {
        result.details.map(detail => revideDetail(detail))
        resolve(result)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        throw errorThrown
      })
  })
}

export function findById(id) {
  return new Promise(resolve => {
    const url = config.API_URL + '/details/' + id
    console.log('url:' + url)
    $.getJSON(url)
      .done(result => {
        if (result.status != 'success') {
          console.log(`Detail no[${id}] not found.`)
          return resolve(null)
        }
        const detail = revideDetail(result.detail)
        resolve(detail)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        throw errorThrown
      })
  })
}

export function findByGovernmentNo(government, no) {
  return new Promise(resolve => {
    const url = config.API_URL + '/details/' + government + '/' + no
    console.log('url:' + url)
    $.getJSON(url)
      .done(result => {
        if (result.status != 'success') {
          console.log(`Detail [${government},${no}] not found.`)
          return resolve(null)
        }
        const detail = revideDetail(result.detail)
        resolve(detail)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        throw errorThrown
      })
  })
}
