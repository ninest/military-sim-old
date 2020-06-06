from rich import print

def show_alerts(state, military):
  alerts = []
  # every 10 years, all reservists leave the army
  if (state.rounds_complete % 5 == 0) and (state.rounds_complete != 0):
    # clear the number of reservists, but only updated in table next year
    military.left_this_year += military.clear_reservists()
    alerts.append('Reservists are leaving soon')

  # print alerts if there are any
  if alerts:
    print('\n[bold]Alerts: [\bold]')
    for alert in alerts:
      print(f'- {alert}')
