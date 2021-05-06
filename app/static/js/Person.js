import { API_URL } from '/static/js/config.js'
import { getQueryString } from '/static/js/util.js'

const revisePerson = person => {
  // person.release_date = moment(person.release_date)
  Object.keys(person).filter(k => k.match(/_date$/)).map(k => {
    person[k] = person[k] && person[k] != 'unknown' ? moment(person[k]) : ''
  })

  return person
}

export function find(option = {}) {
  return new Promise(resolve => {
    const url = getQueryString(API_URL + '/persons', option)
    console.log('URL=' + url)

    $.getJSON(url)
      .done(result => {
        result.current_date = moment(result.current_date)
        result.persons.map(person => revisePerson(person))
        resolve(result)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        resolve(false)
      })
  })
}

export function findByNo(no) {
  return new Promise(resolve => {
    const url = API_URL + '/persons/' + no
    console.log('url:' + url)
    $.getJSON(url)
      .done(result => {
        if (result.status != 'success') {
          console.warn(`findByNo: ${result.message}`)
          resolve(false)
        }
        const person = revisePerson(result.person)
        resolve(person)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        resolve(false)
      })
  })
}

export function getTree(no) {
  return new Promise(resolve => {
    const option = {}
    if (no) option.no = no
    const url = getQueryString(API_URL + '/persons/tree', option)
    console.log('url:' + url)
    $.getJSON(url)
      .done(result => {
        if (result.status != 'success') {
          console.warn(`getTree: ${result.message}`)
          resolve(false)
        }
        const tree = result.tree
        resolve(tree)
      })
      .fail((jqXHR, textStatus, errorThrown) => {
        console.log('Fail', jqXHR, textStatus)
        resolve(false)
      })
  })
}
