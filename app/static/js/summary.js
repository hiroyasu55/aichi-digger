import { API_URL } from '/static/js/config.js'
import { getQueryString } from '/static/js/util.js'

export function getCount(key) {
  return new Promise(resolve => {
    const params = {'key': key}
    const url = getQueryString(API_URL + '/summary/count', params)

    $.getJSON(url)
      .done(result => {
        result.current_date = moment(result.current_date)
        resolve(result)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        resolve(false)
      })
  })
}

export function getCross(row, col) {
  return new Promise(resolve => {
    const params = {'row': row, 'col': col}
    const url = getQueryString(API_URL + '/summary/cross', params)

    $.getJSON(url)
      .done(result => {
        if (result.status != 'success') {
          console.log('Fail', result.message)
          resolve(false)
        }
        result.current_date = moment(result.current_date)
        resolve(result)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        resolve(false)
      })
  })
}
