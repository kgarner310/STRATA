import React, { useState } from 'react'

export default function Roster({ players, setPlayers, gameLog }) {
  const [newName, setNewName] = useState('')

  function addPlayer(e) {
    e.preventDefault()
    const name = newName.trim()
    if (!name || players.includes(name)) return
    setPlayers(prev => [...prev, name].sort())
    setNewName('')
  }

  function removePlayer(name) {
    const gamesPlayed = gameLog.filter(r => r.player_name === name).length
    if (gamesPlayed > 0) {
      if (!confirm(`${name} has ${gamesPlayed} game entries. Remove from roster?`)) return
    }
    setPlayers(prev => prev.filter(p => p !== name))
  }

  return (
    <div>
      <h2 className="section-title">Roster</h2>

      <form onSubmit={addPlayer} className="add-player-row">
        <input
          type="text"
          placeholder="Player name"
          value={newName}
          onChange={e => setNewName(e.target.value)}
        />
        <button type="submit" className="btn btn-primary" disabled={!newName.trim()}>
          Add
        </button>
      </form>

      <div className="card">
        {players.length === 0 ? (
          <p className="message">No players yet. Add your first player above.</p>
        ) : (
          players.map(name => (
            <div key={name} className="player-item">
              <span>{name}</span>
              <button className="btn btn-danger" onClick={() => removePlayer(name)}>
                Remove
              </button>
            </div>
          ))
        )}
      </div>

      {players.length > 0 && (
        <p style={{ color: '#666', fontSize: '0.8rem', textAlign: 'center' }}>
          {players.length} player{players.length !== 1 ? 's' : ''} on roster
        </p>
      )}
    </div>
  )
}
