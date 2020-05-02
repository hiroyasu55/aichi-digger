export function getQueryParams() {
  const queryString = location.search
  if (!queryString.match(/^\?/)) return {}

  const query = queryString.replace(/^\?/, '').split('&')
  const result = {}
  query.map(q => {
    const kv = q.split('=')
    result[kv[0]] = kv.length >= 2 ? kv[1] : ''
  })
  return result
}

export function getJapaneseHolidays() {
  return new Promise(resolve => {
    $.get("https://holidays-jp.github.io/api/v1/date.json", holidays => {
      resolve(holidays)
    })
  })
}
