import React, { useState } from 'react'
import { supabase } from '../supabaseClient'

const STAT_FIELDS = [
  { key: 'at_bats', label: 'AB' },
  { key: 'hits', label: 'H' },
  { key: 'singles', label: '1B' },
  { key: 'doubles', label: '2B' },
  { key: 'triples', label: '3B' },
  { key: 'home_runs', label: 'HR' },
  { key: 'rbi', label: 'RBI' },
  { key: 'runs', label: 'R' },
  { key: 'walks', label: 'BB' },
  { key: 'strikeouts', label: 'K' },
]

export default function GameEntry({ players, onSaved }) {
  const today = new Date().toISOString().split('T')[0]
  const [gameDate, setGameDate] = useState(today)
  const [playerName, setPlayerName] = useState(players[0] || '')
  const [stats, setStats] = useState(
    Object.fromEntries(STAT_FIELDS.map(f => [f.key, 0]))
  )
  const [saving, setSaving] = useState(false)
  const [message, setMessage] = useState('')

  function updateStat(key, value) {
    setStats(prev => ({ ...prev, [key]: parseInt(value) || 0 }))
  }

  async function handleSubmit(e) {
    e.preventDefault()
    if (!playerName || !gameDate) return

    setSaving(true)
    setMessage('')

    try {
      const { error } = await supabase.from('venom').insert({
        player_name: playerName,
        game_date: gameDate,
        ...stats,
      })

      if (error) throw error

      setMessage(`Saved ${playerName}'s stats for ${gameDate}`)
      setStats(Object.fromEntries(STAT_FIELDS.map(f => [f.key, 0])))
      onSaved()
    } catch (err) {
      setMessage(`Error: ${err.message}`)
    } finally {
      setSaving(false)
    }
  }

  if (players.length === 0) {
    return <p className="message">Add players to the roster first.</p>
  }

  return (
    <div>
      <h2 className="section-title">Log Game Stats</h2>

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Date</label>
          <input
            type="date"
            value={gameDate}
            onChange={e => setGameDate(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Player</label>
          <select value={playerName} onChange={e => setPlayerName(e.target.value)}>
            {players.map(p => (
              <option key={p} value={p}>{p}</option>
            ))}
          </select>
        </div>

        <div className="stat-grid">
          {STAT_FIELDS.map(f => (
            <div key={f.key} className="form-group">
              <label>{f.label}</label>
              <input
                type="number"
                min="0"
                value={stats[f.key]}
                onChange={e => updateStat(f.key, e.target.value)}
              />
            </div>
          ))}
        </div>

        <button type="submit" className="btn btn-primary" disabled={saving}>
          {saving ? 'Saving...' : 'Save Game Stats'}
        </button>

        {message && (
          <p className="message" style={{ marginTop: 12, color: message.startsWith('Error') ? '#f87171' : '#4ade80' }}>
            {message}
          </p>
        )}
      </form>
    </div>
  )
}
