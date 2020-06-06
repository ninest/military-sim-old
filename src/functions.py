from rich import print

def show_alerts(military, state):
  alerts = []
  # every 10 years, all reservists leave the army
  if (state.rounds_complete % 5 == 0) and (state.rounds_complete != 0):
    alerts.append('Reservists are leaving soon')

  # print alerts if there are any
  if alerts:
    print('\n[bold]Alerts: [\bold]')
    for alert in alerts:
      print(f'- {alert}')
