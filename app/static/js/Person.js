import { API_URL } from '/static/js/config.js'

const revisePerson = person => {
  person.release_date = moment(person.release_date)
  return person
}

export function find(option = {}) {
  return new Promise(resolve => {
    const params = []
    if (option.offset) params.push({key: 'offset', value: option.offset})
    if (option.limit) params.push({key: 'limit', value: option.limit})

    const url = [API_URL + '/persons', params.map(p => p.key + '=' + p.value).join('&')].join('?')
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

export function getTree() {
  return new Promise(resolve => {
    const url = API_URL + '/persons/tree'
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
