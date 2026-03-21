import React, { useMemo } from 'react'

export default function SeasonStats({ gameLog, loading }) {
  const aggregated = useMemo(() => {
    const byPlayer = {}

    for (const row of gameLog) {
      if (!byPlayer[row.player_name]) {
        byPlayer[row.player_name] = {
          name: row.player_name,
          games: 0,
          at_bats: 0,
          hits: 0,
          singles: 0,
          doubles: 0,
          triples: 0,
          home_runs: 0,
          rbi: 0,
          runs: 0,
          walks: 0,
          strikeouts: 0,
        }
      }
      const p = byPlayer[row.player_name]
      p.games++
      p.at_bats += row.at_bats || 0
      p.hits += row.hits || 0
      p.singles += row.singles || 0
      p.doubles += row.doubles || 0
      p.triples += row.triples || 0
      p.home_runs += row.home_runs || 0
      p.rbi += row.rbi || 0
      p.runs += row.runs || 0
      p.walks += row.walks || 0
      p.strikeouts += row.strikeouts || 0
    }

    return Object.values(byPlayer)
      .map(p => ({
        ...p,
        avg: p.at_bats > 0 ? (p.hits / p.at_bats).toFixed(3) : '.000',
        obp: (p.at_bats + p.walks) > 0
          ? ((p.hits + p.walks) / (p.at_bats + p.walks)).toFixed(3)
          : '.000',
        slg: p.at_bats > 0
          ? ((p.singles + p.doubles * 2 + p.triples * 3 + p.home_runs * 4) / p.at_bats).toFixed(3)
          : '.000',
      }))
      .sort((a, b) => parseFloat(b.avg) - parseFloat(a.avg))
  }, [gameLog])

  if (loading) return <p className="message">Loading...</p>
  if (aggregated.length === 0) return <p className="message">No game data yet. Log your first game.</p>

  return (
    <div>
      <h2 className="section-title">Season Stats</h2>

      <div className="table-scroll">
        <table className="stats-table">
          <thead>
            <tr>
              <th>Player</th>
              <th>G</th>
              <th>AB</th>
              <th>H</th>
              <th>AVG</th>
              <th>HR</th>
              <th>RBI</th>
              <th>R</th>
              <th>BB</th>
              <th>K</th>
              <th>OBP</th>
              <th>SLG</th>
            </tr>
          </thead>
          <tbody>
            {aggregated.map(p => (
              <tr key={p.name}>
                <td>{p.name}</td>
                <td>{p.games}</td>
                <td>{p.at_bats}</td>
                <td>{p.hits}</td>
                <td>{p.avg}</td>
                <td>{p.home_runs}</td>
                <td>{p.rbi}</td>
                <td>{p.runs}</td>
                <td>{p.walks}</td>
                <td>{p.strikeouts}</td>
                <td>{p.obp}</td>
                <td>{p.slg}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
