import React, { useState, useEffect } from 'react'
import { supabase } from './supabaseClient'
import Roster from './components/Roster'
import GameEntry from './components/GameEntry'
import SeasonStats from './components/SeasonStats'
import Charts from './components/Charts'
import Lineup from './components/Lineup'

const TABS = [
  { key: 'roster', label: 'Roster' },
  { key: 'game', label: 'Game' },
  { key: 'stats', label: 'Stats' },
  { key: 'charts', label: 'Charts' },
  { key: 'lineup', label: 'Lineup' },
]

export default function App() {
  const [tab, setTab] = useState('roster')
  const [players, setPlayers] = useState([])
  const [gameLog, setGameLog] = useState([])
  const [loading, setLoading] = useState(true)

  const connected = !!supabase

  useEffect(() => {
    if (connected) {
      fetchData()
    } else {
      setLoading(false)
    }
  }, [connected])

  async function fetchData() {
    setLoading(true)
    try {
      const { data, error } = await supabase
        .from('venom')
        .select('*')
        .order('game_date', { ascending: false })

      if (error) throw error
      setGameLog(data || [])

      const uniquePlayers = [...new Set((data || []).map(r => r.player_name))].sort()
      setPlayers(uniquePlayers)
    } catch (err) {
      console.error('Fetch error:', err)
    } finally {
      setLoading(false)
    }
  }

  function renderTab() {
    if (!connected) {
      return (
        <div className="connection-warning">
          Supabase not configured. Set VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY environment variables to connect.
        </div>
      )
    }

    switch (tab) {
      case 'roster':
        return <Roster players={players} setPlayers={setPlayers} gameLog={gameLog} />
      case 'game':
        return <GameEntry players={players} onSaved={fetchData} />
      case 'stats':
        return <SeasonStats gameLog={gameLog} loading={loading} />
      case 'charts':
        return <Charts gameLog={gameLog} />
      case 'lineup':
        return <Lineup players={players} />
      default:
        return null
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>VENOM</h1>
        <p>Softball Stat Tracker</p>
      </header>

      {renderTab()}

      <nav className="tab-bar">
        {TABS.map(t => (
          <button
            key={t.key}
            className={tab === t.key ? 'active' : ''}
            onClick={() => setTab(t.key)}
          >
            {t.label}
          </button>
        ))}
      </nav>
    </div>
  )
}
