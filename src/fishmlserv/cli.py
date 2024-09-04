from fishmlserv.model.manager import get_model_path, run_prediction
import typer
import fire


def ppping():
  print("pong")

def model_path():
  # typer.run(get_model_path)
  fire.Fire(get_model_path)

def pp():
  fire.Fire(run_prediction)

def ppp():
  typer.run(run_prediction)
