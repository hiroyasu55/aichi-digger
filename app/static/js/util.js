export function getQueryParams(queryString = null) {
  queryString = queryString || location.search
  if (!queryString.match(/^\?/)) return {}

  const query = queryString.replace(/^\?/, '').split('&')
  const result = {}
  query.map(q => {
    const kv = q.split('=')
    result[kv[0]] = kv.length >= 2 ? decodeURI(kv[1]) : ''
  })
  return result
}

export function getQueryString(url, params = {}) {
  const str = [
    url,
    Object.keys(params)
      .filter(key => params[key])
      .map(key => key + '=' + params[key]).join('&')
  ].join('?')
  return str
}

export function getJapaneseHolidays() {
  return new Promise(resolve => {
    $.get("https://holidays-jp.github.io/api/v1/date.json", holidays => {
      resolve(holidays)
    })
  })
}

export class Loader {
  constructor (area) {
    this.area = area
    this.area.empty()
    this.area.append($('<div class="loading-spinner">'))
  }

  start() {
    this.area.removeClass('loading-stop').addClass('loading-start')
  }

  stop() {
    this.area.removeClass('loading-start').addClass('loading-stop')
  }
}
