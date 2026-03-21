import React, { useMemo } from 'react'
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell
} from 'recharts'

const GREEN = '#4ade80'
const DARK_GREEN = '#166534'

function aggregate(gameLog) {
  const byPlayer = {}
  for (const row of gameLog) {
    if (!byPlayer[row.player_name]) {
      byPlayer[row.player_name] = { name: row.player_name, at_bats: 0, hits: 0, home_runs: 0, rbi: 0, runs: 0 }
    }
    const p = byPlayer[row.player_name]
    p.at_bats += row.at_bats || 0
    p.hits += row.hits || 0
    p.home_runs += row.home_runs || 0
    p.rbi += row.rbi || 0
    p.runs += row.runs || 0
  }
  return Object.values(byPlayer).map(p => ({
    ...p,
    avg: p.at_bats > 0 ? +(p.hits / p.at_bats).toFixed(3) : 0,
  }))
}

function LeaderChart({ data, dataKey, title }) {
  const sorted = [...data].sort((a, b) => b[dataKey] - a[dataKey]).slice(0, 8)
  if (sorted.length === 0) return null

  return (
    <div className="chart-container">
      <h3>{title}</h3>
      <ResponsiveContainer width="100%" height={200}>
        <BarChart data={sorted} layout="vertical" margin={{ left: 60, right: 16, top: 4, bottom: 4 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#222" />
          <XAxis type="number" stroke="#444" tick={{ fill: '#888', fontSize: 12 }} />
          <YAxis type="category" dataKey="name" stroke="#444" tick={{ fill: '#ccc', fontSize: 12 }} width={55} />
          <Tooltip
            contentStyle={{ background: '#111', border: '1px solid #333', borderRadius: 8 }}
            labelStyle={{ color: '#4ade80' }}
          />
          <Bar dataKey={dataKey} radius={[0, 4, 4, 0]}>
            {sorted.map((_, i) => (
              <Cell key={i} fill={i === 0 ? GREEN : DARK_GREEN} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default function Charts({ gameLog }) {
  const data = useMemo(() => aggregate(gameLog), [gameLog])

  if (data.length === 0) {
    return <p className="message">No game data yet. Log your first game to see charts.</p>
  }

  return (
    <div>
      <h2 className="section-title">Leaderboards</h2>
      <LeaderChart data={data} dataKey="avg" title="Batting Average" />
      <LeaderChart data={data} dataKey="home_runs" title="Home Runs" />
      <LeaderChart data={data} dataKey="rbi" title="RBI" />
      <LeaderChart data={data} dataKey="runs" title="Runs" />
      <LeaderChart data={data} dataKey="hits" title="Hits" />
    </div>
  )
}
