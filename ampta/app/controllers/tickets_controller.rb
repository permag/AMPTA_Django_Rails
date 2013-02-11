class TicketsController < ApplicationController
  before_filter :confirm_user_new, :only => [:new, :create]
  before_filter :confirm_user_edit, :only => [:edit, :update, :destroy]
  before_filter :sidenav

  def index
    @tickets = Ticket.where("project_id == ?", params[:project_id])
  end

  def show
    @ticket = Ticket.find(params[:id])

    # is ticket or project owner
    if @ticket.user_id == session[:user_id] || @ticket.project.owner_id == session[:user_id]
      @owner_menu = true
    end
  end

  def new
    @ticket = Ticket.new
  end

  def create
    @ticket = Ticket.new(params[:ticket])
    @ticket.user_id = session[:user_id]

    respond_to do |format|
      if @ticket.save
        format.html { redirect_to project_path(@ticket.project), :notice => "Ticket \"#{@ticket.name}\" was created." }
      else
        format.html { render :action => "new" }
      end
    end
  end

  def edit
    @ticket = Ticket.find(params[:id])
  end

  def update
    @ticket = Ticket.find(params[:id])
    respond_to do |format|
      if @ticket.update_attributes(params[:ticket])
        format.html { redirect_to project_ticket_path(@ticket.project, @ticket), :notice => "Ticket \"#{@ticket.name}\" was updated." }
      else
        format.html { render :action => "edit" }
      end
    end
  end

  def destroy
    @ticket = Ticket.find(params[:id])
    @ticket.destroy

    respond_to do |format|
      format.html { redirect_to project_path(@ticket.project), :notice => 'Ticket was deleted.' }
    end
  end

  ##
  # check to see if user is ticket owner or project owner
  #
  def confirm_user_edit
    project = Project.find(params[:project_id])
    ticket =  Ticket.find(params[:id])
    unless ticket.user_id == session[:user_id] || ticket.project.owner_id == session[:user_id] || project.owner_id == session[:user_id]
      flash[:notice] = "You don't have the permission to do that."
      redirect_to home_error_path
      return false
    else
      return true
    end
  end

  def confirm_user_new
    project = Project.find(params[:project_id]) 
    unless project.owner_id == session[:user_id] || project.users.exists?(session[:user_id])
      flash[:notice] = "You don't have the permission to do that."
      redirect_to home_error_path
      return false
    else
      return true
    end
  end

end
